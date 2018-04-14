def insertion_sort(list1):
    for index in range(1, len(list1)):

        current_value = list1[index]
        position = index

        while position > 0 and list1[position-1] > current_value:
            list1[position] = list1[position-1]
            position -= 1

        list1[position] = current_value

A_LIST = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(A_LIST)
print(A_LIST)
