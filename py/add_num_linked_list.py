import unittest


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def num_to_list_node(num):
    first = None
    node = None
    assert num >= 0, "Expecting +ve integer, got {}".format(num)
    if num == 0:
        return ListNode(num)

    while num:
        val = num % 10
        num = num / 10
        new_node = ListNode(val)
        if first is None:
            first = new_node
        else:
            node.next = new_node
        node = new_node
    return first


def from_list_to_num(listNode):
    num = 0
    node_count = 0
    while listNode:
        num += (listNode.val * (10 ** node_count))
        listNode = listNode.next
        node_count += 1
    return num


def traverse_list(listNode):
    nums = []
    while listNode:
        nums.append(listNode.val)
        listNode = listNode.next
    return nums


def solution1(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    num1 = from_list_to_num(l1)
    num2 = from_list_to_num(l2)
    total = num1 + num2
    print "Total: {}".format(total)
    node = num_to_list_node(total)
    return node


def solution2(l1, l2):
    carry = 0
    count = 0
    first = None
    curr = None
    while l1 or l2:
        # get the value
        val1 = (l1.val if l1 else 0)
        val2 = (l2.val if l2 else 0)
        # move to next node
        l1 = (l1.next if l1 else None)
        l2 = (l2.next if l2 else None)

        total = carry + val1 + val2
        carry, val = divmod(total, 10)
        node = ListNode(val)
        if first is None:
            first = node
        else:
            curr.next = node

        curr = node
    return first


class TestSolution(unittest.TestCase):

    def check_solution(self, num1, num2, expected):
        test_name = "Running {}".format(self._testMethodName)
        print("\n %s" % test_name)
        print("-" * (len(test_name) + 2))
        l1 = num_to_list_node(num1)
        l2 = num_to_list_node(num2)
        expected = traverse_list(num_to_list_node(expected))

        print traverse_list(l1)
        print traverse_list(l2)

        sol1 = solution1(l1, l2)
        sol1 = traverse_list(sol1)
        sol2 = solution2(l1, l2)
        sol2 = traverse_list(sol2)

        print "Sol1: ", sol1
        print "Sol2: ", sol2
        print "exp : ", expected

        self.assertEqual(sol1, expected)
        self.assertEqual(sol2, expected)

    def test_01(self):
        num1 = 342
        num2 = 465
        expected = 807

        self.check_solution(num1, num2, expected)

    def test_02(self):
        num1 = 2437992347923749723742397
        num2 = 498579273498723748923749323248
        expected = 498581711491071672673473065645

        self.check_solution(num1, num2, expected)

    def test_03(self):
        num1 = 0
        num2 = 0
        expected = 0

        self.check_solution(num1, num2, expected)


if __name__ == '__main__':
    unittest.main()
