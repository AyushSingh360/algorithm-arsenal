from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = -(10**9)  # effectively -infinity

        for i, x in enumerate(nums):
            if x == 1:
                if i - prev - 1 < k:
                    return False
                prev = i

        return True
