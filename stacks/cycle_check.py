class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None


def cycle_check(node):

    # set both runners at the first node
    runner1 = node
    runner2 = node

    while runner2 != None and runner2.nextnode != None:

        runner1 = runner1.nextnode
        # runner2 runs twice as fast
        runner2 = runner2.nextnode.nextnode

        if runner2 == runner1:
            return True

    return False


# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a  # Cycle Here!

print(cycle_check(a))

# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z

print(cycle_check(x))
