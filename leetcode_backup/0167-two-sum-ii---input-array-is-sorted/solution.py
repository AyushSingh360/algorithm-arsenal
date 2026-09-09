from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]  # 1-indexed as required
            elif s < target:
                l += 1
            else:
                r -= 1

        # Problem guarantees exactly one solution, so this is not really reached.
        return []
