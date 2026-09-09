class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        # is_pal[i][j] = True if s[i:j+1] is a palindrome
        is_pal = [[False] * n for _ in range(n)]

        # Precompute palindromes: expand on length
        for i in range(n):
            is_pal[i][i] = True
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and (length == 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True

        # dp[i] = minimum cuts needed for s[:i+1]
        dp = [0] * n
        for i in range(n):
            # If s[0..i] is a palindrome, no cut needed
            if is_pal[0][i]:
                dp[i] = 0
            else:
                # Try all possible previous cut positions
                dp[i] = i  # worst case: cut before every char
                for j in range(1, i + 1):
                    if is_pal[j][i]:
                        dp[i] = min(dp[i], dp[j - 1] + 1)

        return dp[n - 1]
