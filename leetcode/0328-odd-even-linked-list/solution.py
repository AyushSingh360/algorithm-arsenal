# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head  # head of odd-indexed list (1st, 3rd, 5th, ...)
        even = head.next  # head of even-indexed list (2nd, 4th, 6th, ...)
        even_head = even  # save to attach at the end

        while even and even.next:
            # Link odd to the next odd node
            odd.next = even.next
            odd = odd.next

            # Link even to the next even node
            even.next = odd.next
            even = even.next

        # Attach even list after the last odd node
        odd.next = even_head

        return head
