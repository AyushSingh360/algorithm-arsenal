from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        min_abs = float("inf")
        neg_count = 0

        for row in matrix:
            for val in row:
                if val < 0:
                    neg_count += 1
                abs_val = abs(val)
                total += abs_val
                if abs_val < min_abs:
                    min_abs = abs_val

        # If we have an even number of negatives, all can be made positive.
        if neg_count % 2 == 0:
            return total
        # Otherwise, one must stay negative: put it on the smallest |value|.
        return total - 2 * min_abs
