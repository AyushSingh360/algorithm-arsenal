from collections import Counter
from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = Counter(nums)

        # The entire array is the only size-k subarray.
        if k == n:
            return max(nums)

        # Every element itself forms one subarray.
        if k == 1:
            return max((x for x, count in freq.items() if count == 1), default=-1)

        # For 1 < k < n, only unique boundary values can qualify.
        candidates = []
        if freq[nums[0]] == 1:
            candidates.append(nums[0])
        if freq[nums[-1]] == 1:
            candidates.append(nums[-1])

        return max(candidates, default=-1)
