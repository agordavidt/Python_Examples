import csv

# Open the file in read mode
with open('myfile.csv', 'r') as f:
	# Create a CSV reader
	reader = csv.reader(f)
	# Iterate over the rows of the file
	for row in reader:
		print(row)
