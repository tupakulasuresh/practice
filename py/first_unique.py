def testFirstUniqChar(s):
    def firstUniqChar(s):
        skip_list = []
        for i, c in enumerate(s):
            if c in skip_list:
                continue
            skip_list.append(c)
            if c  not in s[:i]+s[i+1:]:
                return i
        return -1

    print firstUniqChar('leetcode')
    print firstUniqChar('a')
    print firstUniqChar('cc')
    print firstUniqChar('dddccdbba')
    print firstUniqChar('loveleetcode')


def test_frequencySort():
    def frequencySort(s):
        str_hash = dict()
        for e in s:
            str_hash.setdefault(e, 0)
            str_hash[e] += 1

        new_str = ''
        for e in sorted(str_hash, key=str_hash.get, reverse=True):
            new_str += e * str_hash.get(e)
        return new_str
    print frequencySort('tree')


def test_most_frequent():
    def topKFrequent(nums, k):
        num_hash = dict()
        for i in nums:
            num_hash.setdefault(i, 0)
            num_hash[i] += 1

        return sorted(num_hash, key=num_hash.get, reverse=True)[:k]
    print topKFrequent([1,1,1,2,2,3], 2)
    print topKFrequent([1], 2)
    print topKFrequent([1, 2], 2)


def test_findKthLargest():
    def findKthLargest(nums, k):
        # num_hash = set(nums)
        sorted_nums = sorted(nums)
        print sorted_nums
        return sorted_nums[-k]
    print findKthLargest([3,2,1,5,6,4], 2)
    print findKthLargest([3,2,3,1,2,4,5,5,6], 4)


def test_thirdMax():
    def thirdMax(nums):
        sorted_nums = sorted(set(nums))
        k = 3
        if len(sorted_nums) < k:
            return sorted_nums[-1]
        else:
            return sorted_nums[-3]
    print thirdMax([3, 2, 1])
    print thirdMax([1, 2])
    print thirdMax([2, 2, 3, 1])


def test_add_wihtout_operator():
    def add(a, b):
        while b != 0:
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a
    print add(2, 3)
    print add(-2, 0)

def test_intersection_of_array():
    def intersect(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        new_list = []
        for ele in c1:
            repeat = min(c1.get(ele), c2.get(ele))
            if repeat > 0:
                new_list.extend([ele] * repeat)
        return new_list

    print intersect([1,2,2,1], [2, 2])
    print intersect([4,9,5], [9,4,9,8,4])

def test_intersection_of_array_unique():
    def intersect(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1, nums2 = (nums2, nums1) if len(nums2) <  len(nums1) else (nums1, nums2)
        intersection = []
        for ele in set(nums1):
            if ele in nums2:
                intersection.append(ele)
        return intersection
    print intersect([1,2,2,1], [2, 2])
    print intersect([4,9,5], [9,4,9,8,4])

def test_vowel_swap():
    def reverseVowels(s):
        vowels = 'AaEeIiOoUu'
        i = 0
        j = len(s) - 1
        s = list(s)
        while i < j:
            if s[i] in vowels:
                while j > i and s[j] not in vowels:
                    j =- 1
                if s[j] in vowels:
                    s[i], s[j] = s[j], s[i]
                    j -= 2
            i += 1
        return "".join(s)
    print reverseVowels("hello")
    print reverseVowels("leetcode")
    print reverseVowels("bcd")
    print reverseVowels("aA")
    print reverseVowels("Step on hose-pipes? Oh no, pets.")


def test_zero_swap():
    def moveZeroes(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        size = len(nums)
        while i <= size:
            if nums[i] == 0:
                e = nums.pop(i)
                nums.append(e)
                size -= 1
            else:
                i += 1
        return nums
    print moveZeroes([0,1,0,3,12])

def Test_isHappy():
    def checkHappy(n):
        iter_stop = 20
        while n > 3 and iter_stop > 0:
            iter_stop -= 1
            s = 0
            m = n
            while m > 0:
                s += (m % 10 ) ** 2
                m = m / 10
            n = s
        return iter_stop > 0 and n == 1
    print checkHappy(19)
    print checkHappy(4)

def Test_PlusOne():
    def PlusOne(digits):
        carry = 1
        for i in range(len(digits), 0, -1):
            num = digits[i - 1] + 1
            if num > 9:
                carry = num - 9
                num = 0
            else:
                carry = 0
            digits[i - 1] = num
            if carry == 0:
                break
        if carry:
            digits = [carry] + digits
        return digits

    print PlusOne([9])
    print PlusOne([9, 9])


def Test_permutations():
    def permutation(n):
        if len(n) == 0:
            return []
        elif len(n) == 1:
            return [n]
        l = []
        for i in range(len(n)):
            m = n[i]
            rem = n[:i] + n[i+1:]
            print rem
            for p in permutation(rem):
                l.append([m] + p)
        return l
    print permutation(list('abc'))

def TestFactorial():
    def factorial(n):
        res = n
        if n < 0:
            n = abs(n)
            # taking care of negative numbers
            # -1 * -2 * -3 * -4 = 24
            # -1 * -2 * -3  = -6
            if n % 2 == 0:
                res = abs(n)
        while n > 1:
            n -= 1
            res *= n
        return res
    for i in [5, -1, -3, -5, -4, 0]:
        print i, factorial(i)


def TestBalancedStringSplit(object):
    def balancedStringSplit(s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        r_match = 0
        l_match = 0
        for e in s:
            if e == 'R':
                r_match += 1
                if l_match > 0 and r_match == l_match:
                    l = max(l, r_match)
                    l_match = r_match = 0
            elif e == 'L':
                l_match += 1
                if r_match > 0 and r_match == l_match:
                    l = max(l, r_match)
                    l_match = r_match = 0
            else:
                l_match = r_match = 0
        return l

def TestSqrt():
    def sqrt(n):
        i = 0
        while i*i < n:
            i += 1
        if i * i == n:
            return i
        else:
            i = float(i-1)
            while True:
                avg =((n / i) + i) / 2
                if abs(i - avg)  <= 0.0000000001:
                    break
                i = avg
            return avg
    for i in range(0, 11):
        print i, sqrt(i)


def TestFindUnique():
    def findUnique(nums):
        ele = None
        while nums:
            ele = nums.pop(0)
            curr_len = len(nums)
            i = 0
            while i < len(nums):
                if ele == nums[i]:
                    nums.pop(i)
                else:
                    i += 1
            if i >= curr_len:
                break
        return ele
    print findUnique([2, 2, 1])
    print findUnique([4, 1, 2, 1, 2])
    print findUnique([1, 0, 1])

def TestStrDiff():
    def strDiff(s, t):
        for e in s:
            for i in range(len(t)):
                print e, i
                if t[i] == e:
                    break
            t = t[:i] + t[i+1:]
        return t
    print strDiff('abcd', 'abcde')


def TestMakePalindrome():
    def makePalindrome(s):
        def is_palin(s1):
            return s1 == s1[::-1]

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return is_palin(s[l:r]) or is_palin(s[l+1:r+1])
        return True

    print makePalindrome('eedede')
    print makePalindrome('eeccccbebaeeabebccceea')
    print makePalindrome('aba')
    print makePalindrome('abca')
    print makePalindrome('abcd')
    print makePalindrome('abc')
    print makePalindrome('deeee')

def TestValidPalindrome():
    def validPalindrome(s):
        l, r = 0, len(s) - 1
        while l < r:
            a, b = s[l], s[r]
            if not a.isalnum():
                l += 1
            elif not b.isalnum():
                r -= 1
            elif a.lower() == b.lower():
                r -= 1
                l += 1
            else:
                return False
        return True
    print validPalindrome("A man, a plan, a canal: Panama")
    print validPalindrome("race a car")

def TestFib():
    def TestFibLoop(count):
        def generateFibonacci(n):
            prev = 0
            next = 1
            yield prev
            yield next
            for i in range(n-2):
                tmp = next
                next += prev
                prev = tmp
                yield next
        print list(generateFibonacci(count))

    def TestRecurFib(count):
        def recurFib(n):
            if n < 0:
                return 0
            elif n < 2:
                return n
            else:
                return recurFib(n-1) + recurFib(n-2)
        print [recurFib(n) for n in range(count)]
    count = 12
    TestFibLoop(count)
    TestRecurFib(count)
TestFib()
