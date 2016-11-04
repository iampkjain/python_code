#!/usr/bin/env python2.7

#filter
#lambda
#set
#yield
#recursion
#itertools module

double= (lambda x: x*2)



def myfunc():
	yield(1)
	yield(2)
	yield(3)
	yield(4)
for i in myfunc():
	print i




def fact(x):
	if x == 1:
		return 1;
	else:
		return x*fact(x-1)

fa=fact(4)
print fa
