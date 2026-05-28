from math import gcd

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        # If target is 0, we can always do it by doing nothing
        if target == 0:
            return True

        # If target is more than total capacity, impossible
        if x + y < target:
            return False

        # Otherwise, check gcd condition
        return target % gcd(x, y) == 0
