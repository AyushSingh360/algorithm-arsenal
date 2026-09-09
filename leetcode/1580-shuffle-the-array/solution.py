class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        ans = [0] * (2 * n)
        idx = 0
        for i in range(n):
            ans[idx] = nums[i]  # xi
            ans[idx + 1] = nums[i + n]  # yi
            idx += 2
        return ans
