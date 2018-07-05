print("Hello World");

arr = []

while True:
	line = input();
	if len(line) == 0:
		break;
	else:
		newarr = line.split();
		print(newarr);