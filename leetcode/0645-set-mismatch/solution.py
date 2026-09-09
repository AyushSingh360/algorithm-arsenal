class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        freq = [0] * (n + 1)

        for x in nums:
            freq[x] += 1

        dup = miss = -1
        for i in range(1, n + 1):
            if freq[i] == 2:
                dup = i
            elif freq[i] == 0:
                miss = i

        return [dup, miss]
