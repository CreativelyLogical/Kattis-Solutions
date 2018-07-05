nums = input().split()
order = input()

int_nums = [int(a) for a in nums]

int_nums.sort()

ans = ''

dict = {'A': int_nums[0], 'B': int_nums[1], 'C': int_nums[2]}

for letter in order:
	ans += '{} '.format(dict[letter])

print(ans)