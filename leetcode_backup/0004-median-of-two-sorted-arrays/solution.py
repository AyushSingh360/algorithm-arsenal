from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2

        left, right = 0, m
        while left <= right:
            mid1 = (left + right) // 2
            mid2 = half - mid1

            l1 = float("-inf") if mid1 == 0 else nums1[mid1 - 1]
            r1 = float("inf") if mid1 == m else nums1[mid1]
            l2 = float("-inf") if mid2 == 0 else nums2[mid2 - 1]
            r2 = float("inf") if mid2 == n else nums2[mid2]

            if l1 <= r2 and l2 <= r1:
                if total % 2 == 1:
                    return float(max(l1, l2))
                return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                right = mid1 - 1
            else:
                left = mid1 + 1

        # Should never reach here
        return 0.0
