from collections import Counter
from itertools import accumulate
from bisect import bisect_right
from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        # cnt[x] = frequency of number x in nums
        cnt = Counter(nums)

        # cnt_g[g] = number of pairs with gcd exactly g
        cnt_g = [0] * (mx + 1)

        # Process gcd candidates from largest down to 1
        for g in range(mx, 0, -1):
            # Count how many numbers are multiples of g
            v = 0
            for multiple in range(g, mx + 1, g):
                v += cnt[multiple]
                # subtract pairs already attributed to larger gcds (multiples of g)
                cnt_g[g] -= cnt_g[multiple]

            # Add pairs with gcd divisible by g, then after subtraction
            # this becomes pairs with gcd exactly g
            cnt_g[g] += v * (v - 1) // 2

        # Prefix sums: s[g] = number of pairs with gcd <= g
        prefix = list(accumulate(cnt_g))

        # For each query index q, find smallest g with prefix[g] > q
        return [bisect_right(prefix, q) for q in queries]
