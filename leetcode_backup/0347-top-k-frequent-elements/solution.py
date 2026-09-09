from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)  # value -> frequency

        # Buckets where index = frequency, value = list of numbers
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, f in freq.items():
            buckets[f].append(num)

        res = []
        # Traverse buckets from highest frequency down
        for f in range(len(nums), 0, -1):
            for num in buckets[f]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
