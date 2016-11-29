''' Name: Bazil Muzaffar Kotriwala
   Student ID: 27012336 '''

print('This program computes an approximation for the value of e using the first n+1 terms of the continued fraction','\n')

n = int(input('Enter a non-negative integer for the value of n: '))

y = n + (n/(n+1))               # To calculate the inner most fraction
                                # e.g when n = 2, y = 2 + (2/3)

for i in range(n - 1, 0, -1):   # i is the value in the loop in each iteration
    y = i + (i/y)               # for first iteration y(RHS) will take value of y from line 8
                                # for each iteration other than the first, y(RHS) will take value of y from previous iteration
                                # e.g when n = 2, y = 1 + 1/(2 + (2/3))
approx = 2 + (1/y)              #e.g when n = 2, approx = 2 + 1/(1 + 1/(2 + (2/3)))

print('The approximation for the value of e using the continued fraction is %s' %approx)

