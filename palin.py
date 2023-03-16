'''
Create a file named palin.py and create a function inside called palindrome.
• The function palindrome should take in a list as input.
• The function should return a boolean (True or False), depending on whether the list is a palindrome.
• Your function can assume a list will be inputted.
• You can not use the Python function reverse().
• When you submit, do not have any code that calls palindrome nor should it have any print statements.
Our code will take care of calling your function.
• Be mindful of various list sizes when thinking about how to handle bad input.
Examples:
Input : [1, 2, “Espresso”, “Madeline”, 2, 1]
Output : False
Input : [‘a’, True, False, False, True, ‘a’]
Output : True
Input : [3]
Output : True
'''

def palindrome(list):
    ispalin = False
    if list == list[::-1]:
        ispalin = True
        return ispalin
    else:
        ispalin = False
        return ispalin

