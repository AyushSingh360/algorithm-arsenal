from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            val = abs(nums[i])
            idx = val - 1  # since values are in [1, n]

            # if we've already marked this index as negative,
            # it means 'val' has appeared before → duplicate
            if nums[idx] < 0:
                res.append(val)
            else:
                nums[idx] *= -1  # mark as seen

        return res
