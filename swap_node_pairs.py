# Swap Node swapPairs
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def swapPairs(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    dummy = ListNode(0)
    dummy.next = head
    current = dummy
    while current.next and current.next.next:
        next_one, next_two, next_three = current.next, current.next.next, current.next.next.next
        current.next = next_two
        next_two.next = next_one
        next_one.next = next_three
        current = next_one
    return dummy.next
