# -*- coding: utf-8; -*-

import sys
import os
import os.path
import shutil
import threading
import math

#Copy from this directory:
synchronized_this_directory = "from_this_directory"
#to this place
copy_to_this_place = "to_this_directory"

"""
Get two files - original_file and duplicate_file, than verificated size of this files.
"""
def size_verification(original_file, duplicate_file):
	duplicate_file = os.path.join(duplicate_file, os.path.basename(original_file))
	if os.path.exists(duplicate_file) :
		size_original_file = os.path.getsize(original_file)
		size_duplicate_file = os.path.getsize(duplicate_file)
		if size_original_file == size_duplicate_file:
			return True
		else : 
			return False
	else :
		return False

"""
Show size for two files: original_file and duplicate_file
"""
def progressbar(original_file, duplicate_file):
	while True:
		try:
			size_original_file = os.path.getsize(original_file)
			size_duplicate_file = os.path.getsize(duplicate_file)
			os.system('cls')
			show_progressbar = "File name: %s \nSize (duplicate / original): %10d / %-10d"%(os.path.basename(original_file), size_duplicate_file, size_original_file) 
			print show_progressbar
			if size_original_file == size_duplicate_file : break
		except WindowsError:
			pass

"""
Create analog of original directory in the directory for duplicate
"""
def create_directory(start_path, current_path, where_create):
	get_rel_path = os.path.relpath(current_path, start_path)
	new_directory_path = os.path.join(where_create, get_rel_path)
	if os.path.exists(new_directory_path) is False : os.mkdir(new_directory_path)

"""
Start copy file and call progressbar-func in new thread (th1)
(copy_this_file - копируем_этот_файл, to_this_place - сюда, starting_ctrl_c - стартовая_папка_копируемого файла, starting_ctrl_v - стартовая_папка_дубликата)
"""
def copy_with_progressbar(copy_this_file, to_this_place, starting_ctrl_c):
	rel_path = os.path.relpath(copy_this_file, starting_ctrl_c)
	#Тут надо юзать os.path.join но он ставит прямые слеши, заместь косых, так что юзаем конкатенацию, потом разберусь
	#to_this_place = to_this_place+"/"+rel_path
	to_this_place = os.path.join(to_this_place, rel_path)
	th = threading.Thread(name='th1', target=progressbar, kwargs={'original_file':copy_this_file, 'duplicate_file':to_this_place})
	th.start()
	if size_verification(copy_this_file, to_this_place) is False:
		shutil.copy(copy_this_file, to_this_place)

"""
Recurcive search directory and files
"""
def recurcive_search (same_path) :
	if os.path.isdir(same_path):
		create_directory(synchronized_this_directory, same_path, copy_to_this_place)
		for elements in os.listdir(same_path):
			full_path = os.path.join(same_path, elements)
			recurcive_search(full_path)
	else:
		copy_with_progressbar(same_path, copy_to_this_place, synchronized_this_directory)

#=============================================== RUN ===============================================
for dirs_and_files in os.listdir(synchronized_this_directory) :
	total_path = os.path.join(synchronized_this_directory, dirs_and_files)
	recurcive_search(total_path)

raw_input("Press Enter")
