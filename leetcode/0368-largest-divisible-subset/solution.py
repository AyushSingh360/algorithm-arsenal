from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()  # step 1: sort the array
        n = len(nums)

        dp = [1] * n  # dp[i] = length of best subset ending at i
        prev = [-1] * n  # prev[i] = previous index in that subset

        max_len = 1
        max_idx = 0

        # step 2: fill dp and prev
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > max_len:
                max_len = dp[i]
                max_idx = i

        # step 3: reconstruct subset
        res = []
        idx = max_idx
        while idx != -1:
            res.append(nums[idx])
            idx = prev[idx]

        # order is from largest to smallest because we backtracked
        res.reverse()
        return res
