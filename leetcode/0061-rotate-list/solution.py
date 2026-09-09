# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Edge cases: empty list, single node, or no rotation
        if not head or not head.next or k == 0:
            return head

        # 1) Compute the length and get the tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # 2) Reduce k
        k = k % length
        if k == 0:
            return head

        # 3) Find new tail: (length - k - 1) steps from head
        steps_to_new_tail = length - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next

        # 4) New head is next of new_tail
        new_head = new_tail.next

        # 5) Break and reconnect
        new_tail.next = None
        tail.next = head

        return new_head
