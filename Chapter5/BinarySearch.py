def binary_search(item, list1):

    if len(list1) == 0:
        return False

    pos = len(list1)//2

    print("Current position is : "+str(pos)) # for testing purposes

    if list1[pos] == item:
        return True
    elif list1[pos] < item:
        return binary_search(item, list1[pos+1:])
    else:
        return binary_search(item, list1[:pos])

print(binary_search(14, [2,3,10,12,13]))
