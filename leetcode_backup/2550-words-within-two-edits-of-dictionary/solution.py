from typing import List


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        for q in queries:
            for w in dictionary:
                # Count mismatched characters at the same positions
                diff = 0
                for c1, c2 in zip(q, w):
                    if c1 != c2:
                        diff += 1
                        if diff > 2:  # early stop if already more than 2 edits needed
                            break
                if diff <= 2:
                    ans.append(q)
                    break  # no need to check other dictionary words
        return ans
