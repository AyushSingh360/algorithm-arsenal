# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # 1) Find middle (end of first half)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2) Reverse second half starting from slow.next
        prev = None
        curr = slow.next
        slow.next = None  # split the list into two halves
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 3) Merge first half and reversed second half
        first, second = head, prev
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
