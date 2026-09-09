from typing import List
from collections import deque


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # dp[i] = number of ways to partition nums[0:i]
        dp = [0] * (n + 1)
        dp[0] = 1

        # prefix_sum[i] = dp[0] + ... + dp[i]
        prefix_sum = [0] * (n + 1)
        prefix_sum[0] = 1

        # deques store indices; max_d is decreasing, min_d is increasing
        max_d = deque()
        min_d = deque()

        left = 0  # window is [left, right]

        for right in range(n):
            # add nums[right] to deques
            while max_d and nums[max_d[-1]] < nums[right]:
                max_d.pop()
            max_d.append(right)

            while min_d and nums[min_d[-1]] > nums[right]:
                min_d.pop()
            min_d.append(right)

            # shrink window from the left while invalid
            while nums[max_d[0]] - nums[min_d[0]] > k:
                if max_d[0] == left:
                    max_d.popleft()
                if min_d[0] == left:
                    min_d.popleft()
                left += 1

            # valid start indices for last segment: s in [left, right]
            # in dp index terms: dp[s] where s in [left, right]
            # dp index = s, segment is nums[s:right+1]
            # so dp[right+1] = sum(dp[left:right+1])
            L = left
            R = right

            # sum dp[L..R] via prefix sums
            if L == 0:
                total = prefix_sum[R]
            else:
                total = (prefix_sum[R] - prefix_sum[L - 1]) % MOD

            dp[right + 1] = total
            prefix_sum[right + 1] = (prefix_sum[right] + dp[right + 1]) % MOD

        return dp[n]
