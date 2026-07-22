from typing import List
import math

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        # Start from the integer square root and go downwards
        w = int(math.isqrt(area))
        while w > 0:
            if area % w == 0:
                l = area // w
                return [l, w]
            w -= 1
        # Fallback (should never reach here for area >= 1)
        return [area, 1]
