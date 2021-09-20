class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head is None:
            return None
        if head.next is None:
            return head
        current = head
        res = head.next
        temp1 = None
        while current is not None and current.next is not None:
            if temp1 is not None:
                temp1.next = current.next
            temp1 = current
            temp2 = current.next
            temp1.next = temp2.next
            temp2.next = temp1
            current = temp1.next
        return res
