from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        rem = 0
        for b in nums:
            rem = (rem * 2 + b) % 5
            res.append(rem == 0)
        return res
