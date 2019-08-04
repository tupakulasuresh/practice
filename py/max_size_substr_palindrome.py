import unittest


def longestPalinSubstr(string):
    string = string.strip()
    # empty input, no need to check
    if not string:
        return ""
    # in a string atleast one char can be considered as palindrome
    max_substr_size = 1
    str_len = len(string)
    start = 0

    for i in xrange(1, str_len):
        # scan for palindrome substr of even number length
        left = i - 1
        right = i
        while (left >= 0 and right < str_len and string[left] == string[right]):
            curr_substr_size = right - left + 1
            if curr_substr_size > max_substr_size:
                max_substr_size = curr_substr_size
                start = left
            left -= 1
            right += 1

        # scan for palindrome substr of odd number length
        left = i - 1
        right = i + 1
        while (left >= 0 and right < str_len and string[left] == string[right]):
            curr_substr_size = right - left + 1
            if curr_substr_size > max_substr_size:
                max_substr_size = curr_substr_size
                start = left
            left -= 1
            right += 1

    return string[start:start + max_substr_size]


class TestMaxPalindrome(unittest.TestCase):

    def check_max_palindrome(self, input_str, exp_str):
        got = longestPalinSubstr(input_str)
        print "." * 80
        print "Got : ", got
        print "Exp Len: ", len(exp_str)
        print "Got Len: ", len(got)
        self.assertEqual(got, exp_str)

    def test_01(self):
        input_str = "ecdbbd"
        exp_str = "dbbd"
        self.check_max_palindrome(input_str, exp_str)

    def test_02(self):
        input_str = "cbbd"
        exp_str = "bb"
        self.check_max_palindrome(input_str, exp_str)

    def test_03(self):
        input_str = "babad"
        exp_str = "bab"
        self.check_max_palindrome(input_str, exp_str)

    def test_04(self):
        input_str = ""
        exp_str = ""
        self.check_max_palindrome(input_str, exp_str)

    def test_05(self):
        input_str = "ccd"
        exp_str = "cc"
        self.check_max_palindrome(input_str, exp_str)

    def test_06(self):
        input_str = "abcda"
        exp_str = "a"
        self.check_max_palindrome(input_str, exp_str)

    def test_07(self):
        input_str = "aaabaaaa"
        exp_str = "aaabaaa"
        self.check_max_palindrome(input_str, exp_str)

    def test_08(self):
        input_str = "aabcaaa"
        exp_str = "aaa"
        self.check_max_palindrome(input_str, exp_str)

    def test_9(self):
        input_str = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        exp_str = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        self.check_max_palindrome(input_str, exp_str)


if __name__ == "__main__":
    unittest.main()
