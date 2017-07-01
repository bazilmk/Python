'''Name: Bazil Muzaffar Kotriwala
   Timestamp: 3:40PM 17-Dec-2016
   Reads in the n rows of numbers from a file and stores them in a table (2D list)'''

filename = 'TableNumbers1.txt'
infile = open(filename, 'r')
table = []
for line in infile:
	line = line.split()
	table.append(line)
print(table)