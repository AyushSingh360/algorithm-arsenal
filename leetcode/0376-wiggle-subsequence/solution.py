from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n

        up = 1      # best length ending with last step up
        down = 1    # best length ending with last step down

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1
            # if equal, do nothing

        return max(up, down)
