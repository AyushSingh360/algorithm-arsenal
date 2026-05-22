import math

class Solution:
    def bulbSwitch(self, n: int) -> int:
        # Number of bulbs that remain on is the number of perfect squares ≤ n
        return int(math.isqrt(n))
        # Alternatively (a bit slower for huge n):
        # return int(math.sqrt(n))
