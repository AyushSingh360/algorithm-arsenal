from collections import Counter


class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        ones1 = [
            (r, c)
            for r, row in enumerate(img1)
            for c, value in enumerate(row)
            if value == 1
        ]
        ones2 = [
            (r, c)
            for r, row in enumerate(img2)
            for c, value in enumerate(row)
            if value == 1
        ]

        shifts = Counter()

        for r1, c1 in ones1:
            for r2, c2 in ones2:
                # Shift img1 by this vector to align its 1 with img2's 1.
                shifts[(r2 - r1, c2 - c1)] += 1

        return max(shifts.values(), default=0)
