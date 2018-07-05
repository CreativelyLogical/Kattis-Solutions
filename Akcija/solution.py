import itertools

n = int(input())

c = sorted([int(input()) for i in range(n)], reverse=True)

tot = 0

i = 0

while i + 2 < len(c):
	tot += c[i] + c[i+1]
	i += 3

while i < len(c):
	tot += c[i]
	i += 1

print(tot)



