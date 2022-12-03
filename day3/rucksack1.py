from sys import stdin

def getPriority(itemset):
	item = itemset.pop()
	return ord(item) - 38 if item.isupper() else ord(item) - 96

lines = stdin.readlines()
sum = 0
for line in lines:
	rucksack = list(line.strip())
	compartment1, compartment2 = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
	common = set(compartment1).intersection(set(compartment2))
	sum += (getPriority(common))
print(sum)
