from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        
        # Let P be sum of numbers with '+', N be sum of numbers with '-'
        # We need: P - N = target and P + N = total
        # => 2P = target + total => P = (target + total) / 2
        if (target + total) % 2 != 0 or abs(target) > total:
            return 0
        
        subset_sum = (target + total) // 2
        
        # dp[s] = number of ways to get sum s using some subset of nums
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # one way to make sum 0: choose nothing
        
        for num in nums:
            for s in range(subset_sum, num - 1, -1):
                dp[s] += dp[s - num]
        
        return dp[subset_sum]
