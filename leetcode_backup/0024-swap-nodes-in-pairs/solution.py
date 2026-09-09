class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head and head.next:
            first = head
            second = head.next

            # Swapping
            prev.next = second
            first.next = second.next
            second.next = first

            # Move pointers
            prev = first
            head = first.next

        return dummy.next
