def short_bubble_sort(list1):
    exchange = True
    pass_no = len(list1) - 1

    while pass_no > 0 and exchange:
        exchange = False
        for item_no in range(pass_no):
            if list1[item_no] > list1[item_no+1]:
                exchange = True
                list1[item_no], list1[item_no+1] = list1[item_no+1], list1[item_no]
        pass_no -= 1

A_LIST = [54, 26, 93, 17, 77, 31, 44, 55, 20] # constants are to be named in caps
short_bubble_sort(A_LIST)
print(A_LIST)
