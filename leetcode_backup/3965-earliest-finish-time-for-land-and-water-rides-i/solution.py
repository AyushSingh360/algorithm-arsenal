from typing import List


class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        n, m = len(landStartTime), len(waterStartTime)
        ans = float("inf")

        for i in range(n):
            for j in range(m):
                # Option 1: land i -> water j
                land_end = landStartTime[i] + landDuration[i]
                water_start = max(land_end, waterStartTime[j])
                finish1 = water_start + waterDuration[j]

                # Option 2: water j -> land i
                water_end = waterStartTime[j] + waterDuration[j]
                land_start = max(water_end, landStartTime[i])
                finish2 = land_start + landDuration[i]

                ans = min(ans, finish1, finish2)

        return ans
