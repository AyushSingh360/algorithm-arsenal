from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i: int) -> None:
            # If we've considered all elements, record the current subset
            if i == len(nums):
                res.append(subset.copy())
                return

            # Choice 1: do not include nums[i]
            backtrack(i + 1)

            # Choice 2: include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)

            # Backtrack
            subset.pop()

        backtrack(0)
        return res
