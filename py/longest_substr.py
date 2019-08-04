import unittest

def get_longest_substr(str1):
    def get_sub_str(str1):
        substr = ''
        for ele in str1:
            if ele in substr:
                break
            substr += ele
        return substr

    curr_match = ""
    while str1:
        substr = get_sub_str(str1)
        if len(curr_match) < len(substr):
            curr_match = substr
        str1 = str1[1:]

    return curr_match, len(curr_match)


class TestLongestSubStr(unittest.TestCase):

    def check_longest_substr(self, str1, exp):
        test_name = "Running {}".format(self._testMethodName)
        print("\n %s" % test_name)
        print("-" * (len(test_name) + 2))

        got = get_longest_substr(str1)
        print("str: {}".format(str1))
        print("got: {}".format(got))
        self.assertEqual(exp, got)

    def test_01(self):
        str1 = "abcabcbb"
        exp = ('abc', 3)
        self.check_longest_substr(str1, exp)

    def test_02(self):
        str1 = "bbbbbb"
        exp = ('b', 1)
        self.check_longest_substr(str1, exp)

    def test_03(self):
        str1 = "pwwkew"
        exp = ('wke', 3)
        self.check_longest_substr(str1, exp)

    def test_04(self):
        str1 = ""
        exp = ('', 0)
        self.check_longest_substr(str1, exp)

    def test_05(self):
        str1 = "dvdf"
        exp = ('vdf', 3)
        self.check_longest_substr(str1, exp)


if __name__ == "__main__":
    unittest.main()
