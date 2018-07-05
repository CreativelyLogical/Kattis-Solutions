import re

firstInput = input()
secondInput = input()

if (len(re.findall('a*h', firstInput)[0]) > len(re.findall('a*h', secondInput)[0])):
	print("go")
else:
	print("no")