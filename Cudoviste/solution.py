import sys
import re
args = sys.argv
# print "You inputted {} arguments".format(len(sys.argv))


building = '#'
car = 'X'
free = '.'

# if (len(sys.argv) > 1):
# 	file_name = args[1]
# 	# print "And the file name you entered was {}".format(args[1])
# else:
# 	print "You did not enter a file name"

content = []

arr = []

while True:
	try:
		line = input()
		if len(line) > 0:
			content.append(line)
		elif len(line) == 0:
			break
	except EOFError:
		break

del content[0]

# print(content)

for elt in content:
	tmpArr = []
	for letter in elt:
		tmpArr.append(letter)
	arr.append(tmpArr)

# print(arr)

# print arr

# d = raw_input()

# d = d.decode('unicode-escape')
# d = d.encode('utf-8')

# a = re.split('\n', d)
# del a[0]

# arr = []

# for elt in a:
# 	tmpList = []
# 	for letter in elt:
# 		tmpList.append(letter)
# 	arr.append(tmpList)


output = [0, 0, 0, 0, 0]




for i in range(len(arr)-1):
	for j in range(len(arr[i])-1):
		spotArr = []
		# print "{} {}\n{} {}\n\n".format(arr[i][j], arr[i][j + 1], arr[i + 1][j], arr[i + 1][j + 1])
		freeSpot = 0
		buildingSpot = 0
		carSpot = 0

		spotArr.append(arr[i][j])
		spotArr.append(arr[i][j + 1])
		spotArr.append(arr[i + 1][j])
		spotArr.append(arr[i + 1][j + 1])

		# print "The spotArr is {}".format(spotArr)

		for spot in spotArr:
			if (spot == building):
				buildingSpot = buildingSpot + 1
			elif (spot == car):
				carSpot = carSpot + 1
			elif (spot == free):
				freeSpot = freeSpot + 1
		# print "Now, there are {} freeSpots, {} car spots, and {} buildings".format(freeSpot, carSpot, buildingSpot)
		del spotArr
		if buildingSpot > 0:
			continue
		elif freeSpot == 4:
			output[0] += 1
		elif carSpot == 1:
			output[1] += 1
		elif carSpot == 2:
			output[2] += 1
		elif carSpot == 3:
			output[3] += 1
		elif carSpot == 4:
			output[4] += 1

for spot in output:
	print(spot)


		






