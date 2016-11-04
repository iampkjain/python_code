import curses
curses.initscr()
inpu= curses.has_key('q')
if inpu == 'q':
	exit

'''import msvcrt

while True:
	x = msvcrt.kbhit()
	if x:
		ret = msvcrt.getch()
		print ret.decode()
	else:
		print "No key entered"
else:
	print "Exiting"
'''
