from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # Alice always wins when:
        # - number of piles is even
        # - total number of stones is odd
        # and both play optimally
        return True
