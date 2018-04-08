def listSum(list1):

    if len(list1) == 1:
        return list1[0]
    else:
        return list1[0] + listSum(list1[1:])

print(listSum([1,2,3,4,5]))
