from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        pos = 0  # next even index
        neg = 1  # next odd index

        for x in nums:
            if x > 0:
                ans[pos] = x
                pos += 2
            else:
                ans[neg] = x
                neg += 2

        return ans
