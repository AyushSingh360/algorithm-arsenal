from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Sort the array in non-decreasing order
        nums.sort()

        # Case 1: product of three largest numbers
        prod1 = nums[-1] * nums[-2] * nums[-3]

        # Case 2: product of two smallest (could be negative) and the largest
        prod2 = nums[0] * nums[1] * nums[-1]

        # Return the larger of the two
        return max(prod1, prod2)
