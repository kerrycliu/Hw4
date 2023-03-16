'''Create a file named merge.py and create a function inside called merge.
• The function merge should take in two lists as input.
• The function should return a single sorted list.
• Your function can assume two pre-sorted lists containing only integers will be inputted.
• When you submit, do not have any code that calls merge nor should it have any print statements. Our
code will take care of calling your function.
• Be mindful of various list sizes when thinking about how to handle bad input.
Examples:
Input : [1, 3, 5, 7], [2, 4, 6]
Output : [1, 2, 3, 4, 5, 6, 7]
Input : [1, 2, 3, 5], [1, 2, 4, 5, 6]
Output : [1, 1, 2, 2, 3, 4, 5, 5, 6]'''

def merge(list1, list2):
    newList = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            newList.append(list1[i])
            i += 1
        else:
            newList.append(list2[j])
            j += 1
    newList = newList + list1[i:] + list2[j:]
