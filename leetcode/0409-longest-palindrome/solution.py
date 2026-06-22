class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter

        freq = Counter(s)
        length = len(s)
        odd_count = sum(1 for count in freq.values() if count % 2 == 1)
        if odd_count > 0:
            length -= odd_count - 1
        return length
