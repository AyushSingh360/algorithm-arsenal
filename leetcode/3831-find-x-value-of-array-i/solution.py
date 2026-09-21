from typing import List


class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k  # dp[r] = subarrays ending at previous index with product % k == r

        for num in nums:
            value = num % k
            nxt = [0] * k

            # Start a new subarray containing only num.
            nxt[value] += 1

            # Extend every subarray ending at the previous position.
            for rem in range(k):
                nxt[(rem * value) % k] += dp[rem]

            for rem in range(k):
                ans[rem] += nxt[rem]

            dp = nxt

        return ans
