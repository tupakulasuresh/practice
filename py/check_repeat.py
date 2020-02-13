from collections import Counter

def test_string_repetition():
    def find_repeat(str1):
        strlen = len(str1)
        for s in range(2, strlen / 2 + 1):
            if str1[:s] == str1[-s:] and strlen % s == 0:
                repeat = strlen / s
                if str1[:s] * repeat == str1:
                    print str1[:s], " repeated ", repeat, " times in ", str1
                    return repeat
        print "No repetitions in ", str1
        return -1
    find_repeat("abcabcabc")
    find_repeat("abcdabcd")
    find_repeat("aababaabab")
    find_repeat("abcaabc")
    find_repeat("abcadeabc")


def test_permutations():
    def checkInclusion1(s1, s2):
        from collections import Counter
        sublen = len(s1)
        for i in range(0, len(s2) - sublen + 1):
            substr = s2[i:i+sublen]
            if s1[0] in substr and Counter(s1) == Counter(substr):
                return True
        return False

    def checkInclusion2(s1, s2):
        c1 = Counter(s1)
        c2 = Counter()
        s1_len = len(s1)
        s2_len = 0
        for i, e in enumerate(s2):
            print i, e, c1[e], s1_len, c2[e], s2_len
            if e in c1:
                c2.update(e)
                s2_len += 1
                if c2[e] > c1[e] or s2_len > s1_len:
                    c2[s2[i-s1_len+1]] = c2[s2[i-s1_len+1]] - 1
                    print i-s1_len+1, s2[i-s1_len+1]
                    s2_len -= 1
                if s1_len == s2_len and c2 == c1:
                    return True
            else:
                c2.clear()
                s2_len = 0
        return False

    def checkInclusion(s1, s2):
        status1 = checkInclusion1(s1, s2)
        status2 = checkInclusion2(s1, s2)
        print "checkInclusion1 = ", status1, "checkInclusion2 = ", status2


    checkInclusion("hello", "ooolleoooleh")
    return
    checkInclusion('adc', "dcda")
    checkInclusion('ab', 'eidbaooo')
    checkInclusion('ab', "eidboaoo")
    checkInclusion('a', "b")

test_permutations()
