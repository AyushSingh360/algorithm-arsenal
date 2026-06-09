import heapq
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        min_heap = []

        # Push the first element of each row: (value, row, col)
        for r in range(min(n, k)):  # only need up to k rows
            heapq.heappush(min_heap, (matrix[r][0], r, 0))

        # Pop k-1 elements from the heap
        for _ in range(k - 1):
            val, r, c = heapq.heappop(min_heap)
            # Push the next element in the same row
            if c + 1 < n:
                heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))

        return heapq.heappop(min_heap)[0]
