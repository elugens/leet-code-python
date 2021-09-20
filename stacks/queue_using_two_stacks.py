class Queue2Stacks(object):

    def __init__(self):

        # Two Stacks
        self.instack = []
        self.outstack = []

    def enqueue(self, element):  # In-Stack
        # Fill an element
        self.instack.append(element)
        pass

    def dequeue(self):  # Out-Stack
        # if outstack empty
        if not self.outstack:
            while self.instack:
                # Pop elements for the instack and append to outstack
                self.outstack.append(self.instack.pop())

        return self.outstack.pop()
