# Open the file in read mod
with open('myfile.txt', 'r') as f:
	lines = f.readlines()
	for line in lines:
		print(line)
