# Tree Representation Implementation (lists)
# List of Lists


def BinaryTree(r):
    return [r, [], []]


def insertLeft(root, newBranch):
    t = root.pop(1)

    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])

    return root


def insertRight(root, newBranch):
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])

    return root


def getRootVal(root):
    return root[0]


def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]


r = BinaryTree(3)

print(insertLeft(r, 4))

print(insertLeft(r, 5))

print(insertRight(r, 6))

print(insertRight(r, 7))

print(getLeftChild(r))

print(getRightChild(r))

l = getLeftChild(r)

print(l)

setRootVal(l, 9)

print(r)
