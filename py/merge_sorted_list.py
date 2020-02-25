from __future__ import print_function
import unittest
import random


def x_merge_sorted_list(list1, list2):
    if not list1:
        return list2
    elif not list2:
        return list1

    l1 = 0
    l2 = 0
    list3 = list1[:]
    while l1 < len(list3) and l2 < len(list2):
        # log("List3=%d(total=%d), List2=%d(total=%d)" % (l1, len(list3), l2, len(list2))
        ele1 = list3[l1]
        ele2 = list2[l2]
        # log(ele1, ele2
        if ele1 < ele2:
            l1 += 1
        elif ele1 == ele2:
            l2 += 1
        else:
            list3.insert(l1, ele2)
            l2 += 1
    if l2 < len(list2):
        list3.extend(list2[l2:])

    return list3

def merge_sorted_list(list1, list2):
    list3 = []
    l1 = 0
    l2 = 0
    while l1 < len(list1) and l2 < len(list2):
        if list1[l1] < list2[l2]:
            list3.append(list1[l1])
            l1 += 1
        elif list1[l1] > list2[l2]:
            list3.append(list2[l2])
            l2 += 1
        else:
            list3.append(list1[l1])
            l1 += 1
            l2 += 1
    list3.extend(list1[l1:])
    list3.extend(list2[l2:])
    return list3



class TestMerge(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        self.list1 = None
        self.list2 = None
        self.exp = None
        self.debug = False
        super(TestMerge, self).__init__(*args, **kwargs)

    def log(self, *args):
        if self.debug:
            print(*args)

    def check(self):
        self.log("\nRunning ", self._testMethodName)
        self.log("Merging ", self.list1, self.list2)
        got = merge_sorted_list(self.list1, self.list2)
        self.log("Got: ", got)
        self.log("Exp: ", self.exp)
        self.assertListEqual(self.exp, got)

    def test_both_empty(self):
        self.list1 = []
        self.list2 = []
        self.exp = []
        self.check()

    def test_empty_list2(self):
        self.list1 = [1, 2, 3, 5]
        self.list2 = []
        self.exp = self.list1
        self.check()

    def test_empty_list1(self):
        self.list1 = []
        self.list2 = [4, 6, 7]
        self.exp = self.list2
        self.check()

    def test_list1_max_size(self):
        self.list1 = [1, 2, 3, 5, 7, 8, 9, 10, 11, 12, 13]
        self.list2 = [4, 6, 7]
        self.exp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.check()

    def test_list2_max_size(self):
        self.list1 = [1, 2, 3, 5]
        self.list2 = [4, 5, 20, 30, 40, 50, 60]
        self.exp = [1, 2, 3, 4, 5, 20, 30, 40, 50, 60]
        self.check()

    def test_all_duplicates(self):
        self.list1 = [1, 2, 3, 5]
        self.list2 = [1, 2, 3, 5]
        self.exp = self.list1
        self.check()

    def test_huge_list(self):
        self.list1 = random.sample(range(0, 1000), 300)
        self.list2 = random.sample(range(0, 1000), 400)
        self.list1.sort()
        self.list2.sort()
        self.exp = list(set(self.list1 + self.list2))
        self.exp.sort()
        self.check()
