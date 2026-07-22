import random
import bisect
from typing import List

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        # prefix[i] = total number of integer points in rects[0..i]
        self.prefix = []
        total = 0
        for x1, y1, x2, y2 in rects:
            # number of integer x-coords: x2 - x1 + 1
            # number of integer y-coords: y2 - y1 + 1
            points = (x2 - x1 + 1) * (y2 - y1 + 1)
            total += points
            self.prefix.append(total)
        self.total = total

    def pick(self) -> List[int]:
        # Choose a random integer point index in [1, total]
        target = random.randint(1, self.total)
        # Find which rectangle this point falls into
        idx = bisect.bisect_left(self.prefix, target)
        x1, y1, x2, y2 = self.rects[idx]
        # Pick a random integer point inside this rectangle
        x = random.randint(x1, x2)
        y = random.randint(y1, y2)
        return [x, y]
