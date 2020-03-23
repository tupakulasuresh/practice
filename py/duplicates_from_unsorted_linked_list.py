from LinkedList import LinkedList

l1 = LinkedList()
data = [10, 11, 13, 3, 4, 5, 6, 10, 12]
data = [3]
[l1.append(e) for e in data]
l1.traverse()

ptr1 = l1.head
ptr2 = l1.head.next_node

while ptr1:
    ptr2 = ptr1
    while ptr2.next_node:
        if ptr1.data == ptr2.next_node.data:
            ptr2.next_node = ptr2.next_node.next_node
        else:
            ptr2 = ptr2.next_node
    ptr1 = ptr1.next_node

l1.traverse()