from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        # dp[i][j] = max score difference current player can achieve on nums[i..j]
        dp = [[0] * n for _ in range(n)]

        # Base case: single element subarray, you just take it
        for i in range(n):
            dp[i][i] = nums[i]

        # Fill for increasing lengths
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                left_pick = nums[i] - dp[i + 1][j]
                right_pick = nums[j] - dp[i][j - 1]
                dp[i][j] = max(left_pick, right_pick)

        # If player 1's max advantage from the whole array is >= 0, they can win
        return dp[0][n - 1] >= 0
