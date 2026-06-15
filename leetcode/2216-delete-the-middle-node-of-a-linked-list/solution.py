# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: only one node -> delete it, return empty list
        if head is None or head.next is None:
            return None

        # Dummy simplifies deletion (handles middle at head cleanly)
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # Move fast two steps and slow one step
        # When loop ends, slow is just before middle node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Delete the middle node
        slow.next = slow.next.next

        return dummy.next
