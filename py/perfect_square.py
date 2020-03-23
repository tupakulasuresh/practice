class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        start = 1
        end = num

        while start <= end:
            mid = (start + end) / 2
            mid_square = mid * mid
            if mid_square == num:
                return True
            elif mid_square > num:
                end = mid-1
            else:
                start = mid+1
        return False

s = Solution()
print s.isPerfectSquare(1)
print s.isPerfectSquare(10)
print s.isPerfectSquare(16)
