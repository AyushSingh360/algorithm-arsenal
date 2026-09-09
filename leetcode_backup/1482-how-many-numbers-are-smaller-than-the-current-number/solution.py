class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Since 0 <= nums[i] <= 100
        freq = [0] * 101

        # Count frequency of each number
        for x in nums:
            freq[x] += 1

        # Build prefix sums: prefix[i] = count of numbers < i
        for i in range(1, 101):
            freq[i] += freq[i - 1]

        # For each num, answer is count of numbers strictly smaller
        ans = []
        for x in nums:
            if x == 0:
                ans.append(0)
            else:
                ans.append(freq[x - 1])

        return ans
