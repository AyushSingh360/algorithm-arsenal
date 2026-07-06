from collections import Counter
from typing import List

class Solution:
    def fourSumCount(
        self,
        nums1: List[int],
        nums2: List[int],
        nums3: List[int],
        nums4: List[int]
    ) -> int:
        # Count all possible sums of nums1[i] + nums2[j]
        sum_count = Counter(a + b for a in nums1 for b in nums2)

        # For each sum from nums3[k] + nums4[l], look for its negation
        # in sum_count, because we need a + b + c + d == 0 → a + b == -(c + d)
        result = 0
        for c in nums3:
            for d in nums4:
                result += sum_count.get(-(c + d), 0)

        return result
