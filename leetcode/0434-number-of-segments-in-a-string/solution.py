class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        for i, ch in enumerate(s):
            if ch != ' ' and (i == 0 or s[i - 1] == ' '):
                count += 1
        return count
