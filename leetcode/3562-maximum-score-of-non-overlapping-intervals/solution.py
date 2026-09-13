from bisect import bisect_left
from typing import List


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        # (end, start, weight, original_index)
        events = sorted((r, l, w, i) for i, (l, r, w) in enumerate(intervals))

        n = len(events)
        ends = [r for r, _, _, _ in events]

        # dp[k][i] = (best_total_weight, sorted_original_indices)
        # using only the first i sorted events and choosing at most k events
        dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]

        def better(a, b):
            # Prefer larger weight; on a tie, lexicographically smaller indices.
            if a[0] != b[0]:
                return a if a[0] > b[0] else b
            return a if a[1] < b[1] else b

        for k in range(1, 5):
            for i in range(1, n + 1):
                end, start, weight, idx = events[i - 1]

                # Strictly less: touching endpoints means overlap.
                prev = bisect_left(ends, start, 0, i - 1)

                previous_weight, previous_indices = dp[k - 1][prev]
                take = (
                    previous_weight + weight,
                    tuple(sorted(previous_indices + (idx,))),
                )
                skip = dp[k][i - 1]

                dp[k][i] = better(take, skip)

        return list(dp[4][n][1])
