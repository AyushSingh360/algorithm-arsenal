class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        dp = [0] * 26
        cur = 0

        for i, ch in enumerate(s):
            if i > 0 and (ord(ch) - ord(s[i - 1]) == 1 or (s[i - 1] == 'z' and ch == 'a')):
                cur += 1
            else:
                cur = 1

            idx = ord(ch) - ord('a')
            dp[idx] = max(dp[idx], cur)

        return sum(dp)
