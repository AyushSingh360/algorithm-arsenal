# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)

        less = less_dummy
        greater = greater_dummy
        curr = head

        while curr:
            nxt = curr.next
            curr.next = None

            if curr.val < x:
                less.next = curr
                less = less.next
            else:
                greater.next = curr
                greater = greater.next

            curr = nxt

        less.next = greater_dummy.next
        return less_dummy.next
