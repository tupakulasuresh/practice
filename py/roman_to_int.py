def roman_to_int(rstr):
    r_int_dict = {'I':1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


    num = 0
    rlist = list(rstr.upper())
    while rlist:
        ele1 = rlist.pop(0)
        ele1_val = r_int_dict.get(ele1)
        if rlist:
            ele2 = rlist.pop(0)
            ele2_val = r_int_dict.get(ele2)
            if ele2_val > ele1_val:
                num += ele2_val - ele1_val
                continue
            else:
                rlist.insert(0, ele2)
        num += ele1_val


    print rstr, "->", num
    return num

def test_roman_to_int():
    roman_to_int("III")
    roman_to_int("IV")
    roman_to_int("IX")
    roman_to_int("LVIII")
    roman_to_int("MCMXCIV")


def int_to_roman(num):
    int_r_dict = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    rstr = ''
    num_bkup = num
    for i in [1000, 100, 10, 1]:
        if num < i:
            continue
        multiplier = num / i
        num %= i
        if multiplier == 9:
            rstr += int_r_dict.get(i) + int_r_dict.get(i * 10)
            continue

        if multiplier >= 5:
            rstr += int_r_dict.get(i * 5)
            multiplier -= 5

        if multiplier > 0:
            if multiplier == 4:
                rstr += int_r_dict.get(i) + int_r_dict.get(i * 5)
            else:
                rstr += int_r_dict.get(i) * multiplier
    print num_bkup, "->",  rstr
    return rstr

def test_int_to_roman():
    int_to_roman(1994)
    int_to_roman(54)
    int_to_roman(96)
    int_to_roman(80)
    int_to_roman(90)
    int_to_roman(99)
