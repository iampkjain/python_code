#!/usr/bin/env python2.7

import random
def generate_number():
	num =  random.randint(1,10)
	return num
play= True
num = generate_number()
while(play):
	my_num = input("Guess the number. Lets see how smart you are: ")
	if my_num == num:
		print "Jackpot"
		num = generate_number()
	elif my_num < num:
		print "Try with a higher number"
	else:
		print "Try with a lower number"
	pl= raw_input("Do you want to continue: Y/N")
	if pl == 'Y' or pl == 'y' or pl == '' :
		play = True
	else:
		play = False
else:
	print "Thanks for playing. Look out for more games at paras.com"


