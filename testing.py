#!/usr/bin/env python
#-*- coding: utf-8; -*-

import os

copy_from = "/home/lov3catch/MyPyt/synchro_directory/1"
copy_here = "/home/lov3catch/MyPyt/synchro_directory/copy_here"
temp_from = ""

for file in os.listdir(copy_from) :
	print "-",file
	if os.path.isdir(os.path.join(copy_from, file)):
		temp_from = os.path.join(copy_from, file)
		for file in os.listdir(temp_from):
			print "--",file
			if os.path.isdir(os.path.join(temp_from, file)):
				temp_from = os.path.join(temp_from, file)
				for file in os.listdir(temp_from):
					print "---",file

