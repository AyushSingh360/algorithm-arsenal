from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        # Count frequency of each character
        freq = Counter(word)  # at most 26 entries

        # Sort frequencies in descending order
        counts = sorted(freq.values(), reverse=True)

        ans = 0
        for i, c in enumerate(counts):
            # (i // 8 + 1) = number of presses for this "slot"
            ans += (i // 8 + 1) * c

        return ans
