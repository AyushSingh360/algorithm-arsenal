from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries or duration == 0:
            return 0

        total = 0
        for i in range(len(timeSeries) - 1):
            gap = timeSeries[i + 1] - timeSeries[i]
            # Add either the full duration or the gap if next attack comes sooner
            total += min(gap, duration)

        # Last attack always contributes full duration
        total += duration
        return total
