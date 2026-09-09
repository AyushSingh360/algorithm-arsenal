# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        # Use min-heap to efficiently get the smallest node
        min_heap = []

        # Initialize heap with the first node of each list
        for i, node in enumerate(lists):
            if node:
                # (node value, unique index, node object)
                heapq.heappush(min_heap, (node.val, i, node))

        # Create dummy head for result
        dummy = ListNode(0)
        current = dummy

        # Process nodes in sorted order
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next

            # If this node has a next node, add it to heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next
