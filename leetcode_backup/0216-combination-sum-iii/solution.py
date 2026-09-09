from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start: int, remaining: int) -> None:
            # If we have k numbers:
            if len(path) == k:
                if remaining == 0:
                    res.append(path[:])  # valid combination
                return

            # If remaining < 0, no need to proceed
            if remaining < 0:
                return

            # Try all numbers from 'start' to 9
            for num in range(start, 10):
                # Small pruning: if num > remaining, further nums will also be too big
                if num > remaining:
                    break
                path.append(num)
                backtrack(num + 1, remaining - num)
                path.pop()

        backtrack(1, n)
        return res
