import unittest


def longestValidParentheses(string):
    p_open = 0
    pair = 0
    for e in string:
        if e == '(':
            p_open += 1
        elif e == ')' and p_open > 0:
            p_open -= 1
            pair += 1

    return pair * 2

class TestMaxPalindrome(unittest.TestCase):

    def check_longest_valid_parentheses(self, input_str, exp_size):
        got = longestValidParentheses(input_str)
        print "." * 80
        print "Input  : ", input_str
        print "Exp Len: ", exp_size
        print "Got Len: ", got
        self.assertEqual(got, exp_size)

    def test_01(self):
        input_str = "(()"
        exp_size = 2
        self.check_longest_valid_parentheses(input_str, exp_size)

    def test_02(self):
        input_str = ")()())"
        exp_size = 4
        self.check_longest_valid_parentheses(input_str, exp_size)

    def test_03(self):
        input_str = "()(())"
        exp_size = 6
        self.check_longest_valid_parentheses(input_str, exp_size)

    def test_04(self):
        input_str = "()(()"
        exp_size = 2
        self.check_longest_valid_parentheses(input_str, exp_size)


if __name__ == "__main__":
    unittest.main()
