class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # key: (number of 1 bits, value itself)
        return sorted(arr, key=lambda x: (bin(x).count("1"), x))
