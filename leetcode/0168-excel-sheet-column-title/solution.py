from typing import *


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []

        while columnNumber > 0:
            columnNumber -= 1  # shift to 0-based
            rem = columnNumber % 26
            res.append(chr(ord("A") + rem))
            columnNumber //= 26

        # we built it from least significant to most, so reverse
        res.reverse()
        return "".join(res)
