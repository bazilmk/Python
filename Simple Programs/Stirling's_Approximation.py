''' Name: Bazil Muzaffar Kotriwala
    Timestamp: 11:38pm 14 Dec - 2016
    Computing n factorial using Stirling's Approxmiation'''

import math

n = int(input('Enter the value of n: '))
s_approx = math.sqrt(2 * math.pi * n) * (n / math.e) ** n
y = s_approx / math.factorial(n)
print('The approximation is %s which is %s of the exact answer' %(s_approx, y))