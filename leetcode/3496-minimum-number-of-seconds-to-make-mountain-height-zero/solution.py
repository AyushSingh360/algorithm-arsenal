from typing import List
from math import sqrt


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        # Check if it's possible to remove at least mountainHeight within 'time_limit' seconds [web:27]
        def can_complete_in_time(time_limit: int) -> bool:
            total_height = 0
            for wt in workerTimes:
                # For worker with time wt, max k such that:
                # wt * (1 + 2 + ... + k) = wt * k * (k + 1) / 2 <= time_limit [web:27]
                # => k^2 + k - 2 * time_limit / wt <= 0
                # Using quadratic formula, k = floor( -0.5 + sqrt(0.25 + 2 * time_limit / wt) ) [web:27]
                max_k = int(sqrt(2 * time_limit / wt + 0.25) - 0.5)
                if max_k <= 0:
                    continue
                total_height += max_k
                if total_height >= mountainHeight:
                    return True
            return total_height >= mountainHeight

        # Binary search for minimum time T such that can_complete_in_time(T) is True [web:27]
        left, right = 1, 10**16
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if can_complete_in_time(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
