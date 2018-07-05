inputs = []
studtsAboveAvg = []

while True:
	try:
		line = input()
		if len(line) > 0:
			inputs.append(line)
		elif len(line) == 0:
			break
	except EOFError:
		break

del inputs[0]
# print(inputs)

classrooms = []

for string in inputs:
	classrooms.append([int(s) for s in string.split() if s.isdigit()])

# print(classrooms)

for classroom in classrooms:
	numOfStudents = classroom[0]
	del classroom[0]
	classAvg = 0
	gradeSum = 0
	abvAvgStuds = 0
	abvAvgPercentage = 0
	for studentGrade in classroom:
		gradeSum += studentGrade
	classAvg = gradeSum/numOfStudents
	for student in classroom:
		if student > classAvg:
			abvAvgStuds += 1
	studtsAboveAvg.append(abvAvgStuds/numOfStudents * 100)

# print(studtsAboveAvg)

for studt in studtsAboveAvg:
	print("{:.3f}%".format(round(studt, 3)))



