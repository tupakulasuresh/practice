'''
LinkedList implementation library
'''

class Node(object):

    def __init__(self, data):
        self.next_node = None
        self.data = data


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.last = None
        pass

    def add_node(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.last = node
        else:
            self.last.next_node = node
            self.last = self.last.next_node

    def append(self, data):
        self.add_node(data)

    def prepend(self):
        node = Node(data)
        node.next_node = self.head
        self.head = node

    def traverse(self):
        head = self.head
        while head:
            print head.data,
            head = head.next_node
        print ""
