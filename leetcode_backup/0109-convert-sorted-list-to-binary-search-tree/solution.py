from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        # find middle node and split list into left part [head..prev] and mid.next.. for right
        def get_mid(
            start: Optional[ListNode], end: Optional[ListNode]
        ) -> Optional[ListNode]:
            slow = fast = start
            while fast != end and fast.next != end:
                fast = fast.next.next
                slow = slow.next
            return slow

        def build(
            start: Optional[ListNode], end: Optional[ListNode]
        ) -> Optional[TreeNode]:
            if start == end:
                return None

            mid = get_mid(start, end)
            root = TreeNode(mid.val)
            root.left = build(start, mid)
            root.right = build(mid.next, end)
            return root

        return build(head, None)
