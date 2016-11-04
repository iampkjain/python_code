#! /usr/bin/env python2.7
import random
import string

list_words= ["india", "australia", "england", "brazil"]
alphabets= list(string.ascii_lowercase)
play = True

def hangman_init():
	global chances
	chances=10
	global count_answer
	count_answer= 0
	global ind
	ind = random.randint(0,len(list_words)-1)
	global my_word
	my_word= list_words[ind]
	global guess_list
	guess_list=['_']*len(my_word)
	global word_chars
	word_chars= list(my_word)

while play:
	hangman_init()
	while chances:
		if count_answer == len(my_word):
			print "You win"
			break
		else:
			print "Your word for the day is {0}".format(guess_list)
			ch= raw_input("Enter the letter:")
			if ch in alphabets:
				if ch in word_chars:
					for index,value in enumerate(word_chars):
						if value == ch:
							if guess_list[index] == ch:
								print """You have already entered this answer. Forgot so soon"""
								break
							else:
								guess_list[index]= ch
								count_answer+=1
					print guess_list
				else:
					chances -=1
	
					print "Wrong answer.\nDo remember you are left with {0} chances".format(chances)
			else:
				print "Please enter only alphabets"
	else:
		print "You are done with all your chances. Better luck next time."
		print "The answer is {0}".format(list_words[ind])
	
	ans_play = raw_input("Do you want to play again. Y/N: ")
	if ans_play == 'y' or ans_play == 'Y':
		play = True
	else:
		play = False

else:
	print "Thanks for playing. Do visit paras.com for more games"

