from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 0:
            return 0

        left = [1] * n
        right = [1] * n

        # left to right: handle left neighbor
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1

        # right to left: handle right neighbor
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1

        # each child needs max of left[i], right[i]
        return sum(max(left[i], right[i]) for i in range(n))
