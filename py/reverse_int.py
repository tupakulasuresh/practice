import unittest

# integer range
MAX_INT = 2 ** 31
MIN_INT = -MAX_INT - 1


def reverse_int(x):
    rev = 0
    num = abs(x)
    while num:
        rev = (rev * 10) + num % 10
        num /= 10
    if x < 0:
        rev *= -1
    if rev > MAX_INT or rev < MIN_INT:
        rev = 0
    return rev


class TestIntRev(unittest.TestCase):

    def check_result(self, int1, exp):
        print ""
        print "Executing {}".format(self._testMethodName)

        print "Input Int: {}".format(int1)
        print "Expected : {}".format(exp)
        got = reverse_int(int1)
        print "Computed : {}".format(got)
        self.assertEqual(exp, got)

    def test01(self):
        int1 = 321
        exp = 123
        self.check_result(int1, exp)

    def test02(self):
        int1 = 120
        exp = 21
        self.check_result(int1, exp)

    def test03(self):
        int1 = 87123456789
        exp = 0
        self.check_result(int1, exp)

    def test04(self):
        int1 = -243
        exp = -342
        self.check_result(int1, exp)


if __name__ == '__main__':
    unittest.main()
