from typing import List
from collections import Counter


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = 10
        n = len(s)
        if n < L:
            return []

        count = Counter()
        res = []

        # iterate over all 10-letter substrings
        for i in range(n - L + 1):
            sub = s[i : i + L]
            count[sub] += 1
            # add only when it becomes 2 so each appears once in result
            if count[sub] == 2:
                res.append(sub)

        return res
