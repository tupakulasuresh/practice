'''
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: Truee
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
'''

from collections import Counter

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.replace(" ", "").strip()
        if not s or len(s) == 1:
            return True
        c1 = Counter(s)
        odd_count_items = [item for item in c1.iteritems() if item[1] % 2 != 0]
        print odd_count_items
        return len(odd_count_items) <= 2

s = Solution()
print s.validPalindrome("tebbem")