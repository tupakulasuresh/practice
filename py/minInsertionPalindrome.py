'''
1312. Minimum Insertion Steps to Make a String Palindrome
Hard

168

5

Add to List

Share
Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.



Example 1:

Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we don't need any insertions.
Example 2:

Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
Example 3:

Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".
Example 4:

Input: s = "g"
Output: 0
Example 5:

Input: s = "no"
Output: 1


Constraints:

1 <= s.length <= 500
All characters of s are lower case English letters.
'''

from collections import Counter
import unittest


class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        s = s.replace(" ", "").strip()
        # if string is empty or a single char, no insertions required
        if not s or len(s) == 1:
            return 0

        # make a counter to find out the odd count of characters
        c1 = Counter(s)
        # find characters with odd count size
        odd_count_items = [item for item in c1.iteritems() if item[1] % 2 != 0]
        print odd_count_items, " ==> ", len(odd_count_items)
        return max(0, len(odd_count_items) - 1)


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()

    def verify(self):
        result = self.s.minInsertions(self.input_str)
        print "Expected min insertions = %d, computed = %d" % (self.expected, result)
        self.assertEqual(self.expected, result)

    def test01(self):
        self.input_str = "zzazz"
        self.expected = 0
        self.verify()

    def test02(self):
        self.input_str = "mbadm"
        self.expected = 2
        self.verify()

    def test03(self):
        self.input_str = "zjveiiwvc"
        self.expected = 4
        self.verify()


if __name__ == "__main__":
    unittest.main()

