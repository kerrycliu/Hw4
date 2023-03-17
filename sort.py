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
