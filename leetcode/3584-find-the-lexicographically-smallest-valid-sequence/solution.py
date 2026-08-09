from typing import List


class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)

        # suffix[i] = maximum number of trailing characters of word2
        # that can be matched using word1[i:].
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1]
            matched = suffix[i + 1]

            if matched < m and word1[i] == word2[m - 1 - matched]:
                suffix[i] += 1

        ans = []
        j = 0
        used_change = False

        for i, ch in enumerate(word1):
            if j == m:
                break

            # Take an exact match whenever it is available.
            if ch == word2[j]:
                ans.append(i)
                j += 1

            # Otherwise, use the one allowed replacement only if every
            # remaining target character can still be matched afterward.
            elif not used_change and suffix[i + 1] >= m - j - 1:
                ans.append(i)
                j += 1
                used_change = True

        return ans if j == m else []
