from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        def rob_linear(arr: List[int]) -> int:
            prev = 0  # best up to house i-2
            curr = 0  # best up to house i-1
            for x in arr:
                prev, curr = curr, max(curr, prev + x)
            return curr

        # Exclude last or exclude first
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
