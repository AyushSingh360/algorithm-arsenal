from typing import List
from bisect import bisect_right


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n = len(events)

        starts = [e[0] for e in events]
        suf = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suf[i] = max(suf[i + 1], events[i][2])

        ans = 0
        for s, e, v in events:
            j = bisect_right(starts, e)
            ans = max(ans, v + suf[j], v)

        return ans
