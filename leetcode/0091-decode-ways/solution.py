class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == "0":
            return 0

        # dp[i-2] and dp[i-1]
        prev2, prev1 = 1, 1  # dp[0] = 1 (empty), dp[1] depends on s[0] != '0'

        for i in range(1, n):
            curr = 0

            # Single-digit decode (s[i])
            if s[i] != "0":
                curr += prev1

            # Two-digit decode (s[i-1:i+1])
            two = int(s[i - 1 : i + 1])
            if 10 <= two <= 26:
                curr += prev2

            if curr == 0:
                return 0

            prev2, prev1 = prev1, curr

        return prev1
