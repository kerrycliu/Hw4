def palindrome(list):
    ispalin = False
    if list == list[::-1]:
        ispalin = True
        return ispalin
    else:
        ispalin = False
        return ispalin

