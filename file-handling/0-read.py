# Open the file in read mod
with open('myfile.txt', 'r') as f:
	# Read the contnets of the file and store it in a variable
	contents = f.read()
	# Print the contents of the file
	print(contents)
