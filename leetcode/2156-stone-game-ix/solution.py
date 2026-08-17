from typing import List

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = [0, 0, 0]

        for stone in stones:
            cnt[stone % 3] += 1

        # An even number of remainder-0 stones does not change turn parity.
        if cnt[0] % 2 == 0:
            return cnt[1] > 0 and cnt[2] > 0

        # With an odd number of remainder-0 stones, Alice needs
        # a sufficiently large imbalance between remainder 1 and 2.
        return abs(cnt[1] - cnt[2]) > 2
