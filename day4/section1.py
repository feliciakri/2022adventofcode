from sys import stdin

def getAssignments(srange):
	start, end = [int(x) for x in srange.split('-')]
	return (list(range(start, end + 1)))

lines = stdin.readlines()
sum = 0
for line in lines:
	a, b = line.strip().split(',')
	arra, arrb = getAssignments(a), getAssignments(b)
	subset = (all(x in arrb for x in arra)) or (all(x in arra for x in arrb))
	sum += 1 if subset else 0
print (sum)

