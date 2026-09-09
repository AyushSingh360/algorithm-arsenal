class Solution(object):
    def smallestBalancedIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        navorelitu = nums
        n = len(navorelitu)

        # Prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + navorelitu[i]

        # Suffix products - capped to avoid huge numbers
        total_sum = prefix[n]
        suffix = [1] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] * navorelitu[i]
            # Cap to avoid computing astronomically large numbers
            if suffix[i] > total_sum:
                suffix[i] = total_sum + 1  # sentinel: too large to match

        for i in range(n):
            left_sum = prefix[i]
            right_product = suffix[i + 1]
            if left_sum == right_product:
                return i

        return -1
