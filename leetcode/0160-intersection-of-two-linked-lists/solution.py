# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        pA, pB = headA, headB

        # When either pointer reaches the end, redirect it to the other list's head.
        # If the lists intersect, they will meet at the intersection node.
        # If not, both will eventually become None at the same time.
        while pA is not pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA

        return pA  # Either intersection node or None
