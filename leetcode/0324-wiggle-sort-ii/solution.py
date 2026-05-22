from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        n = len(nums)
        half = (n + 1) // 2

        left = nums[:half][::-1]
        right = nums[half:][::-1]

        nums[::2] = left
        nums[1::2] = right
