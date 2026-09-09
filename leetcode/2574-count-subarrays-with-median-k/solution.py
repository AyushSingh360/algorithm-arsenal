from typing import List
from collections import defaultdict


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # find index of k
        idx = nums.index(k)

        # balance -> count for right side
        counter = defaultdict(int)
        balance = 0
        # include empty suffix with balance 0
        counter[0] = 1

        # process to the right of k
        for i in range(idx + 1, n):
            if nums[i] > k:
                balance += 1
            else:
                balance -= 1
            counter[balance] += 1

        ans = 0
        balance = 0

        # process from k to the left, combining with right side
        for i in range(idx, -1, -1):
            if nums[i] > k:
                balance += 1
            elif nums[i] < k:
                balance -= 1
            # need right-balance = -balance or -balance + 1
            ans += counter[-balance] + counter[-balance + 1]

        return ans
