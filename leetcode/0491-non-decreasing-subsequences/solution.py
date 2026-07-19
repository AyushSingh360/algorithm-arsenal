from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start: int, path: List[int]) -> None:
            # If current subsequence length >= 2, record it
            if len(path) >= 2:
                res.append(path[:])

            # Set to avoid duplicates at this recursion level
            used = set()

            for i in range(start, len(nums)):
                # Skip if we've already tried nums[i] at this depth
                if nums[i] in used:
                    continue

                # Enforce non-decreasing condition
                if path and nums[i] < path[-1]:
                    continue

                used.add(nums[i])
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res
