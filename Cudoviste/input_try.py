import re

content = []

sentinel = ""

while True:
	line = input()
	if len(line) > 0:
		content.append(line)
	elif len(line) == 0:
		break
print(content)


