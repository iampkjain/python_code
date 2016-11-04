#!/usr/bin/env python2.7
import random

rollit= True
while rollit:
	print "roll the die"
	no_die = input("Enter the number of die to roll: ")
	l1=[]
	while(no_die):	
		l1.append(random.randint(1,6))
		no_die-=1;
	print l1
	print "Do you want to roll the die again\n"
	ans= raw_input("Y/N")
	if ans=='Y' or ans == 'y':
		rollit= True
	else:
		 rollit= False
else:
	print "Thank you"
