from collections import Counter
from math import isqrt
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        f = Counter(nums)
        ones = f.pop(1, 0)
        ans = (ones - 1) | 1 if ones else 1  # best odd count of 1s, or at least 1 [page:1]

        for x in list(f):
            r = isqrt(x)
            if r * r == x and f.get(r, 0) > 1:
                continue  # chain is better starting from r [page:1]

            cur, cnt = x, 0
            while cur <= 31622 and f.get(cur, 0) > 1:
                cnt += 2
                cur *= cur
            ans = max(ans, cnt + (1 if cur in f else -1))  # optional center [page:1]

        return ans
