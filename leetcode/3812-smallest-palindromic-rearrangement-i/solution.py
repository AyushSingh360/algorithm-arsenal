class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        half = []
        mid = ""

        for i in range(26):
            c = chr(97 + i)
            half.extend(c * (cnt[i] // 2))
            if cnt[i] % 2:
                mid = c

        left = "".join(half)
        return left + mid + left[::-1]
        
