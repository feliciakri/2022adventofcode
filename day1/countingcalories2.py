from sys import stdin
import heapq

def main():
	lines = stdin.readlines()
	tsum = 0
	slist = []
	for line in lines:
		n = line.strip()
		if n.isdigit():
			tsum += int(n)
		else:
			slist.append(int(tsum))
			tsum = 0
	tp3 = heapq.nlargest(3, slist)
	print(sum(tp3))

if __name__ == "__main__":
	main()
