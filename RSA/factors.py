import sys

def factors(n):
	"""Returns a list of the two smallest factors of n"""
	# Check if n is even
	if n % 2 == 0:
		return [2, n // 2]
	# if n is odd, try odd numbers until a factor is found
	for i in range(3, int(n ** 0.5) + 1, 2):
		if n % i == 0:
			return [i, n // i]
	# If no factors are found, n is prime
    

def main():
	# Open the file and read each line
	with open(sys.argv[i], 'r') as f:
		for line in f:
			# Parse the number from the line and find its factors 
			n = int(line)
			f1, f2 = factors(n)
			# Print the factors
			print(f"{n}: {f1} x {f2}")

if __name__ == "__main__":
	main()
