from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # Sort to find median
        nums.sort()
        median = nums[len(nums) // 2]
        
        # Sum of absolute differences to median
        return sum(abs(num - median) for num in nums)
