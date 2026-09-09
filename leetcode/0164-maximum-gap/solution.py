from typing import List
from math import inf


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        mn, mx = min(nums), max(nums)
        if mn == mx:
            return 0

        # Minimum possible maximum gap (average gap), bucket size at least 1
        bucket_size = max(1, (mx - mn) // (n - 1))
        bucket_count = (mx - mn) // bucket_size + 1

        # Each bucket keeps [min_in_bucket, max_in_bucket]
        buckets = [[inf, -inf] for _ in range(bucket_count)]

        # Distribute numbers into buckets
        for x in nums:
            idx = (x - mn) // bucket_size
            buckets[idx][0] = min(buckets[idx][0], x)
            buckets[idx][1] = max(buckets[idx][1], x)

        # Scan buckets to find max gap between consecutive non-empty buckets
        max_gap = 0
        prev_max = mn
        for b_min, b_max in buckets:
            if b_min > b_max:  # empty bucket
                continue
            max_gap = max(max_gap, b_min - prev_max)
            prev_max = b_max

        return max_gap
