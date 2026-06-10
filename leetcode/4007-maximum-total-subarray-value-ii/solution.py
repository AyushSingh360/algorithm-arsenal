from typing import List
import heapq
import math


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        LOG = math.floor(math.log2(n)) + 1

        # Build sparse tables for range max and range min
        st_max = [[0] * n for _ in range(LOG)]
        st_min = [[0] * n for _ in range(LOG)]

        for i in range(n):
            st_max[0][i] = nums[i]
            st_min[0][i] = nums[i]

        j = 1
        while (1 << j) <= n:
            length = 1 << j
            half = length >> 1
            for i in range(n - length + 1):
                st_max[j][i] = max(st_max[j - 1][i], st_max[j - 1][i + half])
                st_min[j][i] = min(st_min[j - 1][i], st_min[j - 1][i + half])
            j += 1

        def range_max(l: int, r: int) -> int:
            length = r - l + 1
            p = length.bit_length() - 1
            span = 1 << p
            return max(st_max[p][l], st_max[p][r - span + 1])

        def range_min(l: int, r: int) -> int:
            length = r - l + 1
            p = length.bit_length() - 1
            span = 1 << p
            return min(st_min[p][l], st_min[p][r - span + 1])

        def value(l: int, r: int) -> int:
            return range_max(l, r) - range_min(l, r)

        # Max-heap over subarrays (l, r) using negative value for Python's min-heap
        heap = []
        for l in range(n):
            v = value(l, n - 1)
            heapq.heappush(heap, (-v, l, n - 1))

        ans = 0
        for _ in range(k):
            neg_v, l, r = heapq.heappop(heap)
            v = -neg_v
            ans += v
            if r > l:
                # push the next candidate for this l: (l, r-1)
                nv = value(l, r - 1)
                heapq.heappush(heap, (-nv, l, r - 1))

        return ans
