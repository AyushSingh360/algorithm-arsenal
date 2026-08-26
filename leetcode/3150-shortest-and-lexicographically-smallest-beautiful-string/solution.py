class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        ones = 0
        ans = ""

        for right, ch in enumerate(s):
            if ch == "1":
                ones += 1

            while ones > k:
                if s[left] == "1":
                    ones -= 1
                left += 1

            # Remove unnecessary leading zeros to minimize length.
            while ones == k and s[left] == "0":
                left += 1

            if ones == k:
                candidate = s[left:right + 1]
                if not ans or len(candidate) < len(ans) or (
                    len(candidate) == len(ans) and candidate < ans
                ):
                    ans = candidate

        return ans
