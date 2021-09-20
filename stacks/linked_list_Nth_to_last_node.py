from nose.tools import assert_equal


class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode = None


def nthNode(n, head):  # Trying to find nth to last node

    left = head  # left pointer
    right = head  # right point n nodes ahead

    for i in range(n-1):

        # Edge Case
        if not right.nextnode:
            raise LookupError('Error: n is larger than the linked list')

        right = right.nextnode

    while right.nextnode:  # Reaches the last node

        right = right.nextnode
        left = left.nextnode

    return left


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

n = nthNode(2, a)

print(n.value)

print(nthNode(2, a).value)

####


class TestNLast(object):

    def test(self, sol):

        assert_equal(sol(2, a), d)
        print('ALL TEST CASES PASSED')


# Run tests
t = TestNLast()
t.test(nthNode)
