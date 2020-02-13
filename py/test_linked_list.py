
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

     def __repr__(self):
         return 'val={}, next=({})'.format(self.val, self.next)

     def __str__(self):
         return self.__repr__()

def create_linked_list(nums):
    prev_node = None
    head = None
    for i in nums:
        new_node = ListNode(i)
        if head is None:
            head = new_node
        else:
            prev_node.next = new_node
        prev_node = new_node
    return head

def print_linked_list(head):
    while head:
        print head.val,
        head = head.next
    print ''



def reverseList(head):
    prev_node = None
    while head:
        next_node = head.next
        head.next = prev_node
        prev_node = head
        head = next_node
    return prev_node

def test_linked_list():
    head = create_linked_list(range(1, 6))
    print 'Initial: ', print_linked_list(head)
    print 'Reverse: ', print_linked_list(reverseList(head))


class Stack(object):
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        self._items.pop()

    def peak(self):
        return self._items[-1] if self._items else None

    def isempty(self):
        return not bool(len(self._items))

    def print_stack(self):
        print self._items

def TestParanthesisMatch():
    def test_paranthesis_match(s):
        paran = dict(zip(['(', '[', '{'], [')', ']', '}']))
        st = Stack()
        for e in s:
            if e in paran.keys():
                st.push(e)
            elif e in paran.values():
                if paran.get(st.peak()) == e:
                    prev = st.pop()
                else:
                    return False
        st.print_stack()
        return st.isempty()
    print test_paranthesis_match('([a, (b)])[')

TestParanthesisMatch()
