class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import defaultdict

        value_map = defaultdict(int)

        for key, val in nums1:
            value_map[key] += val
        for key, val in nums2:
            value_map[key] += val

        result = []
        for key in sorted(value_map):
            result.append([key, value_map[key]])

        return result
