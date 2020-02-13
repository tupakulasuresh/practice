import random

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return 'Node({})'.format(self.val)

def insert_node(node, val):
    if node == None:
        return Node(val)
    elif val < node.val:
        node.left = insert_node(node.left, val)
    elif val >  node.val:
        node.right = insert_node(node.right, val)
    return node


def create_bst(values):
    root = None
    for val in values:
        node = insert_node(root, val)
        if root is None:
            root = node
    return root

# DFS (Depth First Traversal)
def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print node.val,
        inorder_traversal(node.right)

def preorder_traversal(node):
    if node is not None:
        print node.val,
        inorder_traversal(node.left)
        inorder_traversal(node.right)

def postorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        inorder_traversal(node.right)
        print node.val,


# BFS (Breadth First or Level order Traversal)
def bfs_traversal(node):
    if node is None:
        return
    queue = list()
    queue.append(node)
    while (len(queue) > 0):
        node = queue.pop(0)
        print node.val,
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

def sort_bst(node, sorted_list):
    if node is not None:
        sort_bst(node.left, sorted_list)
        sorted_list.append(node.val)
        # print node.val,
        sort_bst(node.right, sorted_list)

def TestBST():
    output = []
    input = range(1, 20)
    random.shuffle(input)
    b = create_bst(input)
    sort_bst(b, output)
    print "Input    : ", input
    print "\nBFS      : ",; bfs_traversal(b)
    print "\nInOrder  : ",; inorder_traversal(b)
    print "\nPreOrder : ",; preorder_traversal(b)
    print "\nPostOrder: ",; postorder_traversal(b)
    print "\nSorted   : ", output
