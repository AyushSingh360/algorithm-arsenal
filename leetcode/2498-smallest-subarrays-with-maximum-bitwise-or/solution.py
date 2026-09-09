class Solution(object):
    def smallestSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1] * n
        bit_last_index = [0] * 32  # Stores last seen index of each bit (0-31)

        for i in range(n - 1, -1, -1):
            for bit in range(32):
                if nums[i] & (1 << bit):
                    bit_last_index[bit] = i

            farthest = i
            for bit in range(32):
                if bit_last_index[bit] > farthest:
                    farthest = bit_last_index[bit]

            res[i] = farthest - i + 1

        return res
