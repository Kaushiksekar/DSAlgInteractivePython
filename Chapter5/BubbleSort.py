def bubble_sort(list1):
    for pass_no in range(len(list1)-1, 0, -1):
        for item_no in range(pass_no):
            if list1[item_no] > list1[item_no+1]:
                list1[item_no], list1[item_no+1] = list1[item_no+1], list1[item_no]

A_LIST = [54, 26, 93, 17, 77, 31, 44, 55, 20] # constants are to be named in caps
bubble_sort(A_LIST)
print(A_LIST)
