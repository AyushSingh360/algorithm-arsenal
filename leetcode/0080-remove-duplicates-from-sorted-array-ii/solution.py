from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # index where we will write the next allowed element
        k = 0

        for x in nums:
            # Always keep first two elements, after that only keep if
            # current x is not the same as the element two positions back
            if k < 2 or x != nums[k - 2]:
                nums[k] = x
                k += 1

        return k
