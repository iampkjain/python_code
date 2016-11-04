#!/usr/bin/env python
import sys
ch_dict= {}
with open(sys.argv[1], 'r') as f1:
	cont= f1.read()
	wordlist = list(cont)
	
	for ch in wordlist:
		if ch != ' ' and ch != '\n': 
			ch_dict.setdefault(ch,0)
			ch_dict[ch] +=1

for ch in ch_dict.keys():
	perc= 100* ch_dict[ch]/len(cont)
	print "{0}-{1}-{2}%".format(ch, ch_dict[ch], perc)

		

