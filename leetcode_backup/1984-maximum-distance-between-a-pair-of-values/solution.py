from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0
        n1, n2 = len(nums1), len(nums2)
        ans = 0

        while i < n1 and j < n2:
            # ensure i <= j
            if i > j:
                j += 1
                continue

            if nums1[i] <= nums2[j]:
                ans = max(ans, j - i)
                j += 1
            else:
                i += 1

        return ans
