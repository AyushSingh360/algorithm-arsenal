from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        # dp[i] = best (current player score - other player score)
        # starting from index i
        dp = [0] * (n + 1)  # dp[n] = 0, no stones left

        # Fill from the end towards the front
        for i in range(n - 1, -1, -1):
            best = float('-inf')
            take = 0
            # Try taking 1, 2, or 3 stones
            for k in range(1, 4):
                if i + k > n:
                    break
                take += stoneValue[i + k - 1]
                # Opponent then plays starting at i + k
                best = max(best, take - dp[i + k])
            dp[i] = best

        diff = dp[0]  # Alice starts at index 0
        if diff > 0:
            return "Alice"
        if diff < 0:
            return "Bob"
        return "Tie"
