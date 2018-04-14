def selection_sort(list1):
    for slot_pos in range(len(list1)-1, 0, -1):
        max_position = 0
        for orig_position in range(1, slot_pos+1):
            if list1[orig_position] > list1[max_position]:
                max_position = orig_position

        list1[slot_pos], list1[max_position] = list1[max_position], list1[slot_pos]

A_LIST = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(A_LIST)
print(A_LIST)
