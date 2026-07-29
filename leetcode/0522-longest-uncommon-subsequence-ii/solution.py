from typing import List

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        # Helper: is s a subsequence of t ?
        def is_subsequence(s: str, t: str) -> bool:
            i = j = 0
            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    i += 1
                j += 1
            return i == len(s)

        ans = -1
        n = len(strs)

        for i in range(n):
            s = strs[i]
            uncommon = True
            for j in range(n):
                if i == j:
                    continue
                # If s is a subsequence of strs[j], it's not uncommon
                if is_subsequence(s, strs[j]):
                    uncommon = False
                    break
            if uncommon:
                ans = max(ans, len(s))

        return ans
