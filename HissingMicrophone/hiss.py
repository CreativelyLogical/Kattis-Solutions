import re

word = raw_input()

if re.search('ss', word):
	print "hiss"
else:
	print "no hiss"
