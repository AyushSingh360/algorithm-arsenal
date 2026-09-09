from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ops = 0
        for x in nums:
            r = x % 3
            if r != 0:
                ops += min(r, 3 - r)
        return ops
