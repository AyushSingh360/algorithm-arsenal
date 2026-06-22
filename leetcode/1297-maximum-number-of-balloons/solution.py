from collections import defaultdict


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        mp = defaultdict(int)
        for c in text:
            if c in "balon":
                mp[c] += 1

        # If fewer than 5 distinct characters, can't form even one "balloon"
        if len(mp) < 5:
            return 0

        # Divide counts of 'l' and 'o' by 2
        mp["l"] //= 2
        mp["o"] //= 2

        return min(mp.values())
