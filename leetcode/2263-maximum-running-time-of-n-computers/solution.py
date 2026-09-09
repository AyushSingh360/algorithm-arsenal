from typing import List


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        # Feasibility: can we run n computers for 't' minutes?
        # Each battery contributes at most min(b, t) minutes.
        # We just need total contribution >= n * t.
        def can_run(t: int) -> bool:
            total = 0
            for b in batteries:
                total += min(b, t)
                if total >= n * t:
                    return True
            return total >= n * t

        # Binary search on time.
        # Upper bound: total battery minutes // n (cannot exceed equal split).
        total_power = sum(batteries)
        left, right = 0, total_power // n
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if can_run(mid):
                ans = mid
                left = mid + 1  # try longer
            else:
                right = mid - 1  # try shorter

        return ans
