class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        n = len(nums)
        # Build a string where the i-th bit differs from nums[i][i]
        res = []
        for i in range(n):
            # nums[i][i] is either '0' or '1'; flip it
            res.append("1" if nums[i][i] == "0" else "0")
        return "".join(res)
