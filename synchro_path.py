#!/usr/bin/env python
#-*- coding: utf-8; -*-

import os
import os.path
import shutil

#Вставляем абсолютные пути к папкам, например:
#copy_from = "/home/lov3catch/MyPyt/synchro_directory/copy_from_this_directory"
#copy_here = "/home/lov3catch/MyPyt/synchro_directory/copy_to_this_directory"
copy_from = "копировать из ЭТОЙ папки"
copy_here = "вставить в ЭТУ папку"



dirs = [copy_from]
files = []

def get_dirs(ctrl_c):
	for files in os.listdir(ctrl_c):
		obj_src = os.path.join(ctrl_c, files)
		if os.path.isdir(obj_src):
			dirs.append(obj_src)

def get_files(ctrl_c):
	for same_obj in os.listdir(ctrl_c):
		obj_src = os.path.join(ctrl_c, same_obj)
		if os.path.isfile(obj_src):
			files.append(obj_src)

def create_dirs(ctrl_c, ctrl_v):
	relative_path = ctrl_c.replace(copy_from,"")
	new_dir_src = ctrl_v+relative_path
	try:
		os.mkdir(new_dir_src)
	except OSError:
		pass
	
def copy_files(ctrl_c, ctrl_v):
	#Генерируем путь для копирования файла. Удаляем имя файла из пути ctrl_c
	ctrl_c_path = os.path.dirname(ctrl_c)
	#Генерируем полный путь для копирования
	ctrl_v = ctrl_v +"/"+os.path.relpath(ctrl_c ,copy_from)
	shutil.copy(ctrl_c, ctrl_v)

#===============================GoGORoveRangers!
print "Copying has been beginning. Status: ",

for element in dirs:
	get_dirs(element)
	get_files(element)
	create_dirs(element, copy_here)

for element in files:
	copy_files(element, copy_here)

print "complete."