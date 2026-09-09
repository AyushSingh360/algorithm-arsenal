from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Compare mid with its right neighbor
            if nums[mid] > nums[mid + 1]:
                # We are on a descending slope or at a peak,
                # so the peak lies on the left side (including mid)
                right = mid
            else:
                # We are on an ascending slope,
                # so the peak lies on the right side (excluding mid)
                left = mid + 1

        # left == right is a peak index
        return left
