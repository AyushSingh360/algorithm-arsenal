from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)

        # Initialize with very negative numbers (must pick at least one pair)
        NEG_INF = float("-inf")
        dp = [[NEG_INF] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prod = nums1[i - 1] * nums2[j - 1]

                # Option 1: skip nums1[i-1]
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
                # Option 2: skip nums2[j-1]
                dp[i][j] = max(dp[i][j], dp[i][j - 1])
                # Option 3: take this pair (start new or extend)
                dp[i][j] = max(dp[i][j], prod)
                if dp[i - 1][j - 1] != NEG_INF:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + prod)

        return dp[m][n]
