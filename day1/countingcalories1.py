from sys import stdin

def main():
	
	lines = stdin.readlines()
	sum = 0
	most = 0
	for line in lines:
		n = line.strip()
		if n.isdigit():
			sum += int(n)
		else:
			most = max(sum, most)
			sum = 0

	print(most)

if __name__ == "__main__":
	main()
