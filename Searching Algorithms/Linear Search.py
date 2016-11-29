'''
Name: Bazil Muzaffar Kotriwala
Student ID: 27012336
'''

def LinearSearch(aList):
    for i in range(len(aList)):
        if aList[i] == target:
            return True
    return False


aList = [2,4,6,8,10]
target = int(input('Enter the target value: '))