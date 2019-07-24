import timeit


def test_find_pair(min_num=1, max_num=1000, total=234, repeat=100):
    test_find_pair_code = '''
    def find_pair_naga(list1, sum1):
        out = list()
        list1 = [i for i in set(list1) if i < sum1]
        for i in list1:
            for j in list1:
                if i != j and i + j == sum1:
                    out.append((i, j))


    def find_pair_suresh(list1, sum1):
        out = list()
        # ignore all numbers that are more than sum1
        list1 = [i for i in list(set(list1)) if i < sum1]
        while len(list1) > 1:
            start = list1.pop(0)
            diff = sum1 - start
            if diff in list1:
                out.append((start, diff))
                list1.remove(diff)

    list1 = range({}, {})
    sum1 = {}
    '''

    def measure_time(func_name):
        return timeit.timeit('{}(list1, sum1)'.format(func_name), setup=test_find_pair, number=repeat)

    test_find_pair_code = test_find_pair_code.format(min_num, max_num, total)

    print "Suresh   T : {}".format(measure_time('find_pair_suresh'))
    print "NagaSundar : {}".format(measure_time('find_pair_naga'))


test_find_pair()


def find_pair_suresh(list1, sum1):
    out = list()
    # ignore all numbers that are more than sum1
    list1 = [i for i in set(list1) if i < sum1]
    while len(list1) > 1:
        start = list1.pop(0)
        diff = sum1 - start
        if diff in list1:
            out.append((start, diff))
            list1.remove(diff)

