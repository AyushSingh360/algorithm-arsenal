from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # group duplicates together [web:5]
        res = []
        subset = []

        def backtrack(start: int) -> None:
            res.append(subset[:])  # record current subset

            for i in range(start, len(nums)):
                # skip duplicates at the same recursion depth [web:5][web:9]
                if i > start and nums[i] == nums[i - 1]:
                    continue
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()

        backtrack(0)
        return res
