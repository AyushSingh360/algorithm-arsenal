from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Map each number in nums2 to its next greater element
        next_greater = {}
        stack = []  # will store numbers, maintaining decreasing order

        for num in nums2:
            # While current num is greater than stack top, we found NGE for stack top
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)

        # Remaining elements in stack have no next greater element
        # (they map to -1 by default)

        # Build result for nums1 using the map
        return [next_greater.get(x, -1) for x in nums1]


