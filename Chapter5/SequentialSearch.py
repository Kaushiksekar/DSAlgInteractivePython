def search(item, list1):

    pos = 0

    while pos < len(list1):
        if list1[pos] == item:
            return True
        else:
            pos += 1

    return False

print(search(10, [2,3,4,5,6,7]))
print(search(2, [2,3,4,5,6,7]))
