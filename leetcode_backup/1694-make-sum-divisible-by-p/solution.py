from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_rem = sum(nums) % p
        if total_rem == 0:
            return 0

        n = len(nums)
        last = {0: -1}  # remainder -> last index
        cur = 0
        ans = n

        for i, x in enumerate(nums):
            cur = (cur + x) % p
            target = (cur - total_rem + p) % p
            if target in last:
                ans = min(ans, i - last[target])
            last[cur] = i

        return -1 if ans == n else ans
