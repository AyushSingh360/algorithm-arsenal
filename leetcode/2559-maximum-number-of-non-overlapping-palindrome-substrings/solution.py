class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)

        def is_palindrome(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        for end in range(k, n + 1):
            # Do not use a palindrome ending at `end - 1`
            dp[end] = dp[end - 1]

            # A valid palindrome of length k
            if is_palindrome(end - k, end - 1):
                dp[end] = max(dp[end], dp[end - k] + 1)

            # A valid palindrome of length k + 1
            if end >= k + 1 and is_palindrome(end - k - 1, end - 1):
                dp[end] = max(dp[end], dp[end - k - 1] + 1)

        return dp[n]
