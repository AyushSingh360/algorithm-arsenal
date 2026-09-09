from typing import *


class Solution:
    def pivotInteger(self, n: int) -> int:
        total = n * (n + 1) // 2  # sum 1..n
        x = int(total**0.5)  # candidate pivot

        if x * x == total:  # check x^2 == total
            return x
        return -1
