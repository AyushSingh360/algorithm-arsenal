class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = set()
        upper = set()

        for ch in word:
            if "a" <= ch <= "z":
                lower.add(ch)
            else:  # 'A' <= ch <= 'Z'
                upper.add(ch)

        ans = 0
        for c in range(ord("a"), ord("z") + 1):
            lo = chr(c)
            up = chr(c - 32)  # ASCII: 'a' - 'A' == 32
            if lo in lower and up in upper:
                ans += 1

        return ans
