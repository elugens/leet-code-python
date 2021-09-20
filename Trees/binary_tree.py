# Representing a Tree
# Nodes and References


class BinaryTree(object):

    def __init__(self, rootObj):

        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):

        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightchild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, Obj):
        self.key = Obj

    def getRootVal(self):
        return self.key


r = BinaryTree('a')

print(r.getRootVal())


print(r.getLeftChild())

r.insertLeft('b')

l = r.getLeftChild().getRootVal()

print(l)
