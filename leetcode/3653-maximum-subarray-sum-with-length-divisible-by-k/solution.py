from typing import List


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        INF = 10**18
        # minPrefix[r] = minimum prefix sum seen at indices with index % k == r
        minPrefix = [INF] * k
        # For index -1 (before start), treat remainder (k-1) with prefix sum 0
        minPrefix[k - 1] = 0

        prefix = 0
        ans = -INF

        for i, x in enumerate(nums):
            prefix += x
            r = i % k
            # best subarray ending at i with length multiple of k
            ans = max(ans, prefix - minPrefix[r])
            # update minimum prefix for this remainder
            if prefix < minPrefix[r]:
                minPrefix[r] = prefix

        return ans
