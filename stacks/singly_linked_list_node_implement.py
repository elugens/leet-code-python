class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None


# Pros
# Linked Lists have constant time or O(1) insertions and deletions in any position
# They will also be allowed to expand without having to specify their size ahead of time

# Cons
# In order to access a value in a linked list takes O(k) time to go from the head of the list to the kth element (end of list)
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextnode = b
b.nextnode = c
c.nextnode = d

print(a.nextnode.value)

print(a.nextnode.nextnode.value)

print(a.nextnode.value + b.nextnode.value)

print(a.value)
