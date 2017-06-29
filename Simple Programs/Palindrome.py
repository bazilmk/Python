'''
This program determines whether the String is a palindrome
:raises: The size of the string must be greater than 1
:precondition: There must be a string given
:postcondition: Determines whether the string is a palindrome
:complexity: Best Case O(n)
'''

aString = 'abba'

def isPalindrome(aString):
    result = True
    if len(aString) > 1:
        for i in range(len(aString)//2):
            if aString[i] != aString[-i-1]:
                result = False
        return result

print(isPalindrome(aString))