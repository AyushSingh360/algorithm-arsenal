# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: empty list or single node
        if not head or not head.next:
            return head

        # 1. Split the list into two halves (using slow/fast pointers)
        mid = self._get_mid(head)
        right = mid.next
        mid.next = None  # break the list into [head..mid] and [right..]

        # 2. Sort each half
        left_sorted = self.sortList(head)
        right_sorted = self.sortList(right)

        # 3. Merge the two sorted halves
        return self._merge(left_sorted, right_sorted)

    def _get_mid(self, head: ListNode) -> ListNode:
        # Returns node just before the midpoint (end of left half)
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _merge(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 if l1 else l2
        return dummy.next
