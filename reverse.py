aList = [1, 2, 3, 4]


while aList != []:              # Stack method
    x = aList.pop()
    print(x)


for i in range(-1, -len(aList)-1, -1):     # for loop method
    print(aList[i])