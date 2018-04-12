def sorted_list_search(item, list1):

    pos = 0

    while pos < len(list1):
        print("Position Currently checking : "+str(pos)) # for testing purposes
        if list1[pos] == item:
            return True
        elif list1[pos] > item:
            return False
        else:
            pos += 1

    return False

print("For first search")
print(sorted_list_search(1,[2,3,5,6,7]))
print("For second search")
print(sorted_list_search(5,[2,3,5,6,7]))
print("For third search")
print(sorted_list_search(8,[2,3,5,6,7]))
print("For fourth search")
print(sorted_list_search(4,[2,3,5,6,7]))
