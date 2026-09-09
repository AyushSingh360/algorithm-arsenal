from typing import List
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.indices_map = {}
        for i, n in enumerate(nums):
            if n not in self.indices_map:
                self.indices_map[n] = []
            self.indices_map[n].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.indices_map[target])
