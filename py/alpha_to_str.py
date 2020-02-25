import re
'''
Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
'''


def to_str(s):
    return "".join([chr(96 + int(e.rstrip('#'))) for e in re.findall('\d{2}#|\d', s)])
    def int_to_str(i):
        char_start = 97
        return chr(int(i) + char_start - 1)

    new_str = ''

    i = 0
    while i < len(s):
        if s[i] == '#':
            sub_str = s[0:i]
            s = s[i+1:]
            i = 0
            # when ends with '#', last 2 digits represents one char
            # extract last two numbers and find the equivalent char
            last = sub_str[-2:]
            sub_str = sub_str[:-2]
            new_str += ''.join([int_to_str(c) for c in sub_str])
            new_str += int_to_str(last)
        else:
            i += 1
    # anything remaining will be single digit mapped to char
    new_str += ''.join([int_to_str(c) for c in s])

    return new_str

def test_to_str():
    s = "10#11#12"
    print to_str(s)
    s = "1326#"
    print to_str(s)
test_to_str()


def to_num(str1):
    n_str = ''
    for c in str1:
        n = ord(c) - 96
        if n > 9:
            n_str += str(n) + '#'
        else:
            n_str += str(n)
    return n_str

print to_num('acz')
print to_num('jkab')

