# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Dummy node to handle deletions at the head
        dummy = ListNode(-1, head)
        curr = dummy

        # Traverse while there is a next node to inspect
        while curr.next:
            if curr.next.val == val:
                # Skip the node with matching value
                curr.next = curr.next.next
            else:
                # Move forward only when we don't delete
                curr = curr.next

        # New head might be different if original head was removed
        return dummy.next
