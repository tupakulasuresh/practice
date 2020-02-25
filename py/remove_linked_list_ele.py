import unittest


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return '{}(val={})'.format(self.__class__.__name__, self.val)

    def __repr__(self):
        return self.__str__()


def remove_elements(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    new_head = None
    previous = None

    print "Removing {} from the list".format(val)
    while head:
        if head.val == val:
            if previous:
                previous.next = head.next
        else:
            previous = head
            if new_head is None:
                new_head = head
        head = head.next
    print_linked_list(new_head)
    return new_head

def create_linked_list(eles):
    print "Creating linked list with ", eles
    head = None
    current = None
    for i in eles:
        l = ListNode(i)
        if head is None:
            head = l
            current = l
        else:
            current.next = l
            current = l
    # print_linked_list(head)
    return head

def print_linked_list(head):
    for i in traverse_list(head):
        print i,
    print ""

def traverse_list(head):
    while head:
        yield head.val
        head = head.next


def merge_lists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    if l1.val > l2.val:
        l2, l1 = l1, l2
    head = l1
    l1_prev = l1
    l2_prev = l2
    while l1 and l2:
        while l1 and l1.val <= l2.val:
            l1_prev = l1
            l1 = l1.next
        l1_prev.next = l2
        if l1:
            while l2 and l2.val <= l1.val:
                l2_prev = l2
                l2 = l2.next
            l2_prev.next = l1
    print_linked_list(head)
    return head

class TestMergeSortedList(unittest.TestCase):

    def verify(self, input1, input2):
        print "\n", "=" * 80
        exp_output = sorted(input1 + input2)
        input1 = create_linked_list(input1)
        input2 = create_linked_list(input2)
        got_output = list(traverse_list(merge_lists(input1, input2)))
        print "exp_output: ", exp_output
        print "got_output: ", got_output
        self.assertEquals(exp_output, got_output)

    def test01(self):
        l1 = [2]
        l2 = [1]
        self.verify(l1, l2)

    def test02(self):
        l1 = [2]
        l2 = [3]
        self.verify(l1, l2)

    def test03(self):
        l1 = [1, 2, 4]
        l2 = [1, 3, 4]
        self.verify(l1, l2)

    def test04(self):
        l1 = [1, 2, 5]
        l2 = [3, 4, 6]
        self.verify(l1, l2)

    def test05(self):
        l1 = [1, 2, 2, 6]
        l2 = [3, 4, 5]
        self.verify(l1, l2)

class TestRemoveElement(unittest.TestCase):

    def verify(self, list1, val):
        print "\n", "=" * 80
        exp_output = [ele for ele in list1 if ele != val]
        list1 = create_linked_list(list1)
        got_output = list(traverse_list(remove_elements(list1, val)))
        print "exp_output: ", exp_output
        print "got_output: ", got_output
        self.assertEquals(exp_output, got_output)

    def test01(self):
        self.verify([1], 1)

    def test02(self):
        self.verify([1, 2, 3, 5, 6, 7, 8, 6], 6)


if __name__ == '__main__':
    unittest.main()
