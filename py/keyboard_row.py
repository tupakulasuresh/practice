'''
Given a List of words, return the words that can be typed using letters of
alphabet on only one row's
'''

class Solution(object):
    def findWords(self, words):
        row1 = set('QWERTYUIOP')
        row2 = set('ASDFGHJKL')
        row3 = set('ZXCVBNM')
        output = []

        for word in words:
            w = set(word.upper())
            if w.issubset(row1) or w.issubset(row2) or w.issubset(row3):
                output.append(word)
        return output

    def test(self, words):
        print self.findWords(words)


s = Solution()
s.test(["Hello", "Alaska", "Dad", "Peace"])
