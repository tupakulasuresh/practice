from math import sqrt

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """

        b = int(sqrt(c))
        a = 0
        while a <= b:
            val = a*a + b*b
            if val == c:
                print a, b
                return True
            if val > c:
                b -= 1
            else:
                a += 1
        return False
s = Solution()
print s.judgeSquareSum(5)
print s.judgeSquareSum(3)
