from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # There are only 1440 possible minutes in a day.
        if len(timePoints) > 1440:
            return 0

        times = sorted(
            int(time[:2]) * 60 + int(time[3:])
            for time in timePoints
        )

        minimum = float("inf")

        # Compare adjacent times.
        for i in range(1, len(times)):
            minimum = min(minimum, times[i] - times[i - 1])

        # Compare the last time with the first time across midnight.
        minimum = min(minimum, times[0] + 1440 - times[-1])

        return minimum
