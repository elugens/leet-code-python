class Deque(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


d = Deque()

print(d.isEmpty())

d.addRear(1)

d.addFront(2)

print(d.items)

d.addRear(3)

print(d.items)

d.removeFront()

print(d.items)
