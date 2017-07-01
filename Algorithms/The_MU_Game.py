'''Name: Bazil Muzaffar Kotriwala
   Timestamp: 6:20PM 15 Dec - 2016
   Implementation of the MU Game i.e based on the MU Puzzle'''

# The game has 4 rules, which we need to implement via code for the game to run correctly.
# Game only consists of characters M, U and I
	
string = input('Enter a string comprising of letters M and/or U and/or I: ')
string = string.upper()
L = ['M', 'U', 'I']

# check if string entered is valid

for char in string:
	if char not in L:
		break

while True:

	print('1. Apply Rule 1. ')
	print('2. Apply Rule 2. ')
	print('3. Apply Rule 3. ')
	print('4. Apply Rule 4. ')

	rule = input('Select a rule (1-4) or q to quit ')

	# Rule 1

	if rule == '1':
		if string[-1] == 'I':
			string = string + 'U'
			print('New string is ' + string)

	# Rule 2

	if rule == '2':
		if string[0] == 'M':
			string = string + string[1:]
			print('New string is ' + string)

	# Rule 3

	if rule == '3':
		pos = int(input('State the starting position of substring III you want to replace: '))
		if string[pos:pos+3] == 'III':
			string = string[:pos] + 'U' + string[pos+3:]
			print('New string is ' + string)

	# Rule 4

	if rule == '4':
		pos = int(input('State the position of substring UU you want to delete: '))
		if string[pos:pos+2] == 'UU':
			string = string[:pos] + string[pos+2:]
			print('New string is ' + string)

	if rule == 'q':
		print('The program has been terminated. ')
		break