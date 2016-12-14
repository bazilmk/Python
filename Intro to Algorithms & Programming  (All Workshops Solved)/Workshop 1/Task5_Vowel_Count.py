''' Name: Bazil Muzaffar Kotriwala
    Timestamp: 11:55pm 14 Dec - 2016
    Length of name + Vowel Count'''


name = input('Enter the your username: ')
name_length = len(name)
print('The length of the name is %s' %name_length)

# 5 vowels, therfore 5 vowel counts.

count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

# Loop through name and increment count each time a vowel is found respectively.

for vowel in name:
	if 'a' == vowel:
		count_a += 1
	if 'e' == vowel:
		count_e += 1
	if 'i' == vowel:
		count_i += 1
	if 'o' == vowel:
		count_o += 1
	if 'u' == vowel:
		count_u += 1

print('The number of a\'s in name are ' + str(count_a))
print('The number of e\'s in name are ' + str(count_e))
print('The number of i\'s in name are ' + str(count_i))
print('The number of o\'s in name are ' + str(count_o))
print('The number of u\'s in name are ' + str(count_u))