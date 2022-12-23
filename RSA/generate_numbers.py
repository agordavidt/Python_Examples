# Open the file for writing
with open("numbers.txt', 'w') as f:
	# Write a list of numbers to the fille, one number per line
	for i in range(1, 101):
		f.write(str(i) + '\n')
