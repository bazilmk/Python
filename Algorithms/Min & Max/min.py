'''
Author: Bazil Muzaffar Kotriwala
Timestamp: 04 May 2017 2:00AM
'''

def min_element(array):
    min = array[0]
    for i in range(1, len(array)):
        if array[i] < min:
            min = array[i]

    return min