'''
Author: Bazil Muzaffar Kotriwala
Timestamp: 04 May 2017 2:04AM
'''

def max_element(array):
    max = array[0]
    for i in range(1, len(array)):
        if array[i] > max:
            max = array[i]
    return max