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
    newList += list1[i:] + list2[j:]
    return newList

