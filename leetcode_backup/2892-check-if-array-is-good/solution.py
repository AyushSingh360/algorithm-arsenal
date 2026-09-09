from collections import Counter
from typing import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        # n is determined by the maximum element
        n = max(nums)

        # Length must be n + 1
        if len(nums) != n + 1:
            return False

        cnt = Counter(nums)

        # Values must be exactly from 1 to n
        if set(cnt.keys()) != set(range(1, n + 1)):
            return False

        # 1..n-1 must appear once, n must appear twice
        for x in range(1, n):
            if cnt[x] != 1:
                return False

        return cnt[n] == 2
