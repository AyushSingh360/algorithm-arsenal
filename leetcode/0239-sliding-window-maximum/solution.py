from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # stores indices, nums[dq] is decreasing
        res = []

        for i, x in enumerate(nums):
            # Remove indices outside the current window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Maintain decreasing order in deque
            while dq and nums[dq[-1]] <= x:
                dq.pop()

            dq.append(i)

            # Window becomes valid when i >= k-1
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res
