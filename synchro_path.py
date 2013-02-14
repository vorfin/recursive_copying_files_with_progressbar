# -*- coding: utf-8; -*-

import os
import os.path
import shutil

my_path = os.path.dirname(__file__)

copy_from = "D:/MyPyt/test_dir_2"
copy_to = "D:/MyPyt/test_dir_3"

def copy_file (ctrl_c, ctrl_v, file_name):
	print "COPY "+file_name+" to "+ctrl_v+"",
	shutil.copy(ctrl_c, ctrl_v)
	print " OK"

def make_dir (ctrl_v, file_name):
	try:
		os.mkdir(os.path.join(ctrl_v, file_name))
	except WindowsError:
		print "ERROR"

files_and_catalogs = os.listdir(copy_from)
for file_name in files_and_catalogs :
	absolute_path = os.path.join(copy_from, file_name)
	#Копирование файлов
	if os.path.isfile(absolute_path) :
		copy_file(absolute_path, copy_to,file_name)
	#Создание папок
	if os.path.isdir(absolute_path) :
		make_dir(copy_to, file_name)