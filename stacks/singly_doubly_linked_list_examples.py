class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextnode = b
b.nextnode = c
c.nextnode = d

print(a.nextnode.value)
print(b.nextnode.value)
print(c.nextnode.value)


class DLLNode(object):

    def __init__(self, value):
        self.value = value
        self.prevnode = None
        self.nextnode = None


a.nextnode = b
b.prevnode = a
b.nextnode = c
c.prevnode = b
c.nextnode = d
d.prevnode = c

print(b.prevnode.value)
