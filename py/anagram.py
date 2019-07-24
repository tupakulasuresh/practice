import itertools


def find_count(str1):
    def _find_pattern(main_str):
        pat_count = 0
        while main_str:
            if main_str.startswith(ana):
                pat_count += 1
            main_str = main_str[1:]
        return pat_count

    count = 0
    while str1:
        for size in range(1, len(str1)):
            substr = str1[:size]
            for item in set(itertools.permutations(substr, size)):
                ana = "".join(item)
                print ana
                continue
                count += _find_pattern(str1[1:])
        str1 = str1[1:]
    return count


str_list = ['abba', 'abcd', 'ifailuhkqq', 'kkkk', 'cdcd']
str_list = ['abba']

for str2 in str_list:
    print str2, find_count(str2)


def find_count2(str1):
    count = 0
    possible_substrs = [str1[y:][:x] for y in range(0, len(str1)) for x in range(1, len(str1[y:]) + 1)]
    possible_substrs.remove(str1)
    print possible_substrs

