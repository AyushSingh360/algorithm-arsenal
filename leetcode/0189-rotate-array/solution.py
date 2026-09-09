from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0:
            return

        k %= n  # handle k >= n
        if k == 0:
            return

        # helper to reverse elements in-place between indices l and r inclusive
        def reverse(l: int, r: int) -> None:
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        # 1) reverse entire array
        reverse(0, n - 1)
        # 2) reverse first k elements
        reverse(0, k - 1)
        # 3) reverse the rest
        reverse(k, n - 1)
