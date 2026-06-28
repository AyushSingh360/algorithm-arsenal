class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter

        if len(p) > len(s):
            return []

        p_count = Counter(p)
        window_count = Counter()
        res = []
        left = 0

        for right, ch in enumerate(s):
            window_count[ch] += 1

            if right - left + 1 > len(p):
                left_char = s[left]
                window_count[left_char] -= 1
                if window_count[left_char] == 0:
                    del window_count[left_char]
                left += 1

            if right - left + 1 == len(p) and window_count == p_count:
                res.append(left)

        return res
