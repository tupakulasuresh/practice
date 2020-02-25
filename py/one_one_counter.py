def counter(target):
    '''
    1
    11
    21
    1211
    111221
    312211
    13112221
    1113213211
    '''

    if target <= 0:
        return

    my_list = [1]
    print my_list[0]
    for _ in range(1, target):
        tmp_list = []
        curr = my_list[0]
        count = 0
        for ele in my_list:
            if ele == curr:
                count += 1
            else:
                tmp_list.extend([count, curr])
                curr = ele
                count = 1
        tmp_list.extend([count, curr])
        print "".join(map(str, tmp_list))
        my_list = tmp_list[:]


counter(15)


