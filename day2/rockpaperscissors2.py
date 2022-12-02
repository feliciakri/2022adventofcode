from sys import stdin
ehval_dict = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
msval_dict = {'X': 2, 'Y': 0, 'Z': 1}
point_dict = {0: 3, 1: 6, 2: 0}

lines = stdin.readlines()
point = 0
for line in lines:
	eh, ms = line.split()
	ehval, msval = ehval_dict[eh], msval_dict[ms]
	hval = (msval + ehval) % 3
	hval = 3 if hval == 0 else hval
	point += point_dict[msval] + hval

print(point)



