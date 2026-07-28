import random
from typing import List

class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n      # number of remaining zero cells
        self.mp = {}            # mapping for "swapped" indices

    def flip(self) -> List[int]:
        # pick a random index among remaining candidates [0, total-1]
        self.total -= 1
        x = random.randint(0, self.total)  # inclusive bounds

        # find the real index: if x is mapped, use mp[x], else x itself
        idx = self.mp.get(x, x)

        # move the last available index into position x
        # so x won't be picked again, but we still keep total-1 reachable
        self.mp[x] = self.mp.get(self.total, self.total)

        # convert flattened index back to (row, col)
        return [idx // self.n, idx % self.n]

    def reset(self) -> None:
        # restore full range and clear mapping
        self.total = self.m * self.n
        self.mp.clear()
