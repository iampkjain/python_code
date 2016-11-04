#!/usr/bin/env python2.7
import random

print "roll the die"
#no_die = raw_input("Enter the number of die to roll")
#for die in no_die:
#	l1.append(random.randint(1,6))
num1 = random.randint(1,6)
num2 = random.randint(1,6)
print num1, num2
if num1 == 6 and num2==6:
	print "powbara. Fhek dubara"
	num1 = random.randint(1,6)
	num2 = random.randint(1,6)
	print num1, num2
else:
	print "Next players turn"

