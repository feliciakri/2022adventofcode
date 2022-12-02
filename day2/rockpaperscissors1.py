from sys import stdin
elf_dict = {'A': 1, 'B': 2, 'C': 3}
my_dict = {'X': 1, 'Y': 2, 'Z': 3}
win_dict = {0: 3, 1: 6, 2: 0}

lines = stdin.readlines()
point = 0
for line in lines:
	n, k = line.split()
	e, m = elf_dict[n], my_dict[k]
	val = (m - e) % 3
	
	point += win_dict[val] + m
	#print(line, win_dict[val], m)

print(point)

