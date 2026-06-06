from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = 0
        right_sum = sum(nums)
        result = []
        
        for num in nums:
            right_sum -= num  # Remove current element from right sum
            result.append(abs(left_sum - right_sum))  # Calculate absolute difference
            left_sum += num  # Add current element to left sum
        
        return result
