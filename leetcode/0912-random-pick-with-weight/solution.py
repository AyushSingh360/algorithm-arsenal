import random
import bisect
from typing import List

class Solution:

    def __init__(self, w: List[int]):
        # Build prefix sums: prefix[i] = sum of w[0..i]
        self.prefix = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)
        self.total = total  # sum(w)

    def pickIndex(self) -> int:
        # Pick a random target in [1, total]
        target = random.randint(1, self.total)
        # Find first prefix >= target
        idx = bisect.bisect_left(self.prefix, target)
        return idx
