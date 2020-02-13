import math

"""
492. Construct the Rectangle
Easy

165

237

Add to List


1. The area of the rectangular web page you designed must equal to the given target area.

2. The width W should not be larger than the length L, which means L >= W.

3. The difference between length L and width W should be as small as possible.
You need to output the length L and the width W of the web page you designed in sequence.
Example:
Input: 4
Output: [2, 2]
Explanation: The target area is 4, and all the possible ways to construct it are [1,4], [2,2], [4,1].
But according to requirement 2, [1,4] is illegal; according to requirement 3,  [4,1] is not optimal compared to [2,2]. So the length L is 2, and the width W is 2.
Note:
The given area won't exceed 10,000,000 and is a positive integer
The web page's width and length you designed must be positive integers.
"""

class Solution(object):
    def xconstructRectangle(self, area):
        min_area = None
        min_area_tuple = []
        i = 1
        while i <= area:
            j = 1
            while j <= i:
                if i * j > area:
                    break
                elif i * j == area:
                    if min_area is None or min_area >= i - j:
                        min_area_tuple = [i, j]
                        min_area = i - j
                j += 1
            if min_area_tuple and min_area == 0:
                break
            i += 1
        return min_area_tuple

    def constructRectangle(self, area):
        i = int(math.sqrt(area))
        while i*i <= area:
            if area % i == 0:
                return [area/i, i]
            i -= 1

    def test(self, area):
        print self.constructRectangle(area)


s = Solution()
s.test(4)
