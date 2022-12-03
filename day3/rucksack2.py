from sys import stdin

def getPriority(itemset):
	item = itemset.pop()
	return ord(item) - 38 if item.isupper() else ord(item) - 96

allelves = ([[*line.strip()] for line in stdin.readlines()])
groupsofelves = list(zip(*(iter(allelves),) * 3))

sum = 0
for group in groupsofelves:
	x, y, z = group
	commonitem = (set(x) & set(y) & set(z))
	sum += getPriority(commonitem)
print (sum)
