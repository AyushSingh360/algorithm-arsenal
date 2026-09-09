from typing import List


class Solution:
    def maxOperations(self, s: str) -> int:
        ones = 0
        ans = 0

        for i, ch in enumerate(s):
            if ch == "1":
                ones += 1
            elif i > 0 and s[i - 1] == "1":
                # boundary between a block of 1s and this 0
                ans += ones

        return ans
