'''Create a file named sort.py and create a function inside called sort_dictionary
• The function sort_dictionary should take in a dictionary as input
• Given a dictionary with names as keys and a tuple of phone numbers and age sort by age and output a
list of tuples with only the name and phone number.
• When you submit do not have any code that calls sort_dictionary nor should it have any print
statements. Our code will take care of calling your function.
Examples:
Input : {‘Tom’ : (5464512, 24) , ‘Sara’ : (5446987, 32) , ‘Mary’ : (1557896, 20)}
Output : [(‘Mary’, 1557896), (‘Tom’, 5464512), (‘Sara’, 5446987)]
'''

def sort_dictionary(dictionary):
    # create a list of tuples with name, phone and age
    myTuple = [(name, phone_age[0], phone_age[1]) for name, phone_age in dictionary.items()]

    # sort the tuples list by age
    def sort_by_age(t):
        return t[2]
    sortedList = sorted(myTuple, key=sort_by_age)

    # create a list of tuples with name and phone only
    newList = [(name, phone) for name, phone, age in sortedList]

    return newList
