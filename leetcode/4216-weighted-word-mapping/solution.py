from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = []

        for word in words:
            total = 0
            # sum weights for this word
            for ch in word:
                idx = ord(ch) - ord('a')
                total += weights[idx]

            # reduce modulo 26
            total %= 26

            # reverse alphabetical mapping: 0 -> 'z', 1 -> 'y', ..., 25 -> 'a'
            # so index = 25 - total
            mapped_char = chr(ord('a') + (25 - total))
            res.append(mapped_char)

        return ''.join(res)
