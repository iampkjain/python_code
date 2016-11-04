#!/usr/bin/env python

with open("fl1.txt", 'r') as f1:

	print f1.read()

	f1.seek(0)



	for line in f1:
		print line,
	f1.seek(0)
	
	print f1.readlines()	
