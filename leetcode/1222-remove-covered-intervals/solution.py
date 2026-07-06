from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # 1. Sort by left ascending, and for ties by right descending
        intervals.sort(key=lambda x: (x[0], -x[1]))  # [web:6][web:7][web:10]

        # 2. Scan and count uncovered intervals
        count = 0
        max_right = -1

        for left, right in intervals:
            # If this interval extends beyond all previous rights,
            # it cannot be fully covered by a previous interval.
            if right > max_right:  # [web:10]
                count += 1
                max_right = right
            # If right <= max_right, it is covered by some previous interval. [web:6][web:10]

        return count
