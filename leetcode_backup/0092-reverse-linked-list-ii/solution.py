# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head

        # move prev to node just before 'left'
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next

        curr = prev.next

        # reverse [left, right] using head insertion
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next
