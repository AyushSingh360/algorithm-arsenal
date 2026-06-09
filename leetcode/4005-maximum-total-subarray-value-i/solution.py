from typing import List

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        # Find global min and max in a single pass
        mn = float('inf')
        mx = float('-inf')
        for x in nums:
            if x < mn:
                mn = x
            if x > mx:
                mx = x
        
        best_single = mx - mn   # max value of any single subarray
        return best_single * k  # pick that subarray k times
