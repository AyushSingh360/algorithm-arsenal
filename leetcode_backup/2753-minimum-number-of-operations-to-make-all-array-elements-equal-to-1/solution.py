from typing import List
from math import gcd


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        # Count existing 1s
        ones = sum(1 for x in nums if x == 1)
        if ones > 0:
            # Turn each non-1 into 1 using an adjacent 1
            return n - ones

        # Find minimal length subarray with gcd == 1
        best = n + 1
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == 1:
                    best = min(best, j - i + 1)
                    break

        if best == n + 1:
            return -1

        # (best - 1) ops to create first 1, then (n - 1) to spread it to all positions
        return (best - 1) + (n - 1)
