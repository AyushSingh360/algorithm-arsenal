from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n          # default when no next greater exists
        stack = []              # stack of indices, maintains decreasing values

        # iterate twice to simulate circular array
        for i in range(2 * n):
            curr = nums[i % n]

            # resolve next greater for indices whose value is smaller than curr
            while stack and nums[stack[-1]] < curr:
                idx = stack.pop()
                res[idx] = curr

            # only push indices in the first pass
            if i < n:
                stack.append(i)

        return res
