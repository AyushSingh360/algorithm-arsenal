# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(float("-inf"))
        curr = head

        while curr:
            # Save next node before we change curr.next
            nxt = curr.next

            # Find insertion position starting from dummy
            prev = dummy
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            # Insert curr after prev
            curr.next = prev.next
            prev.next = curr

            # Move to next node in original list
            curr = nxt

        return dummy.next
