# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 1) Find middle using slow/fast
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2) Reverse second half starting at slow
        prev = None
        cur = slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # 3) Compute max twin sum
        ans = 0
        left = head
        right = prev
        while right:  # second half has n/2 nodes
            s = left.val + right.val
            if s > ans:
                ans = s
            left = left.next
            right = right.next

        return ans
