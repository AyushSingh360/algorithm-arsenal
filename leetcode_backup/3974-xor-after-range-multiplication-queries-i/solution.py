from typing import List

MOD = 10**9 + 7


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for l, r, k, v in queries:
            idx = l
            while idx <= r:
                nums[idx] = (nums[idx] * v) % MOD
                idx += k

        ans = 0
        for x in nums:
            ans ^= x
        return ans
