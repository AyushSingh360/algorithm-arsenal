# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # 1. Find middle (slow will be at middle)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse second half starting from slow
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 3. Compare first half (head) and reversed second half (prev)
        first, second = head, prev
        result = True
        while second:  # second half is <= first half in length
            if first.val != second.val:
                result = False
                break
            first = first.next
            second = second.next

        # 4. (Optional) Restore list by reversing second half back
        curr = prev
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # Now list is restored; we don't need to relink explicitly since
        # first half still points into this reversed-back segment.

        return result
