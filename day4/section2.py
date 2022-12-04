from sys import stdin

def getAssignments(srange):
	start, end = [int(x) for x in srange.split('-')]
	return (list(range(start, end + 1)))

lines = stdin.readlines()
sum = 0
for line in lines:
	a, b = line.strip().split(',')
	arra, arrb = getAssignments(a), getAssignments(b)
	overlap = not set(arra).isdisjoint(arrb)
	sum += 1 if overlap else 0
print (sum)
	
