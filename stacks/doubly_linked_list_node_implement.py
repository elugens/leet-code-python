class DoublyLinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None
        self.prevnode = None

# Basic Doubly Linked list diagram

# | header <-> Node1 <-> Node2 <-> Trailer |

# The header and trailer are know as sentinels or guards


a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)
d = DoublyLinkedListNode(4)

a.nextnode = b  # header
b.prevnode = a
b.nextnode = c
c.prevnode = b
c.nextnode = d
d.prevnode = c  # Trailer

print(a.nextnode.value)

print(a.nextnode.nextnode.value)

print(a.value)
