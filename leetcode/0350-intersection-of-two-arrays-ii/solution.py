from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Use Counter to count occurrences in both arrays
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        
        result = []
        # For each common element, add it min(count1, count2) times
        for num in count1:
            if num in count2:
                result.extend([num] * min(count1[num], count2[num]))
        
        return result
