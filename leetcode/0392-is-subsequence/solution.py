class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0  # i for s, j for t
        m, n = len(s), len(t)

        # Empty s is always a subsequence
        if m == 0:
            return True

        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == m
