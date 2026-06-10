# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import random

class Solution:

    def __init__(self, head: Optional[ListNode]):
        # Just store the head; no extra array needed
        self.head = head

    def getRandom(self) -> int:
        # Reservoir sampling for k = 1
        res = None
        i = 1
        curr = self.head

        while curr:
            # With probability 1/i, choose current node's value
            if random.randint(1, i) == 1:
                res = curr.val
            curr = curr.next
            i += 1

        return res
