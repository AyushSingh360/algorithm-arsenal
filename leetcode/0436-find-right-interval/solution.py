from bisect import bisect_left
from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        starts = sorted(iv[0] for iv in intervals)
        pos = {iv[0]: i for i, iv in enumerate(intervals)}
        ans = [-1] * n

        for i, iv in enumerate(intervals):
            j = bisect_left(starts, iv[1])
            if j < n:
                ans[i] = pos[starts[j]]
        return ans
