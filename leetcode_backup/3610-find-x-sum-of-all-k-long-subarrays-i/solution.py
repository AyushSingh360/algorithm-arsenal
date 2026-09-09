from typing import List
from collections import Counter


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []

        for i in range(len(nums) - k + 1):
            freq = Counter(nums[i : i + k])
            arr = sorted(freq.items(), key=lambda p: (-p[1], -p[0]))

            total = 0
            for val, cnt in arr[:x]:
                total += val * cnt

            ans.append(total)

        return ans
