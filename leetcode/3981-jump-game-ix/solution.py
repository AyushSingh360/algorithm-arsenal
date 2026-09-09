class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Build prefix maximum array
        pre_max = [0] * n
        pre_max[0] = nums[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], nums[i])

        # Build answer array using suffix minimum
        ans = [0] * n
        suf_min = float("inf")

        # Traverse from right to left
        for i in range(n - 1, -1, -1):
            if i + 1 < n and pre_max[i] > suf_min:
                # Can connect to right side, propagate answer
                ans[i] = ans[i + 1]
            else:
                # Isolated or rightmost, use prefix max
                ans[i] = pre_max[i]

            # Update suffix minimum
            suf_min = min(suf_min, nums[i])

        return ans
