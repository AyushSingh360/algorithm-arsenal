from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        ans = [""] * n
        order = sorted(range(n), key=lambda i: score[i], reverse=True)

        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]

        for place, idx in enumerate(order):
            if place < 3:
                ans[idx] = medals[place]
            else:
                ans[idx] = str(place + 1)

        return ans
