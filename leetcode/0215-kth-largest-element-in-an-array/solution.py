from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Keep a min-heap of size k with the k largest elements seen so far
        heap = []

        for x in nums:
            if len(heap) < k:
                heapq.heappush(heap, x)
            else:
                if x > heap[0]:
                    heapq.heapreplace(heap, x)

        # The root is the kth largest
        return heap[0]
