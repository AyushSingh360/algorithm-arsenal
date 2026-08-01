class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_seen = {0: -1}
        total = 0
        best = 0

        for i, x in enumerate(nums):
            total += 1 if x == 1 else -1
            if total in first_seen:
                best = max(best, i - first_seen[total])
            else:
                first_seen[total] = i

        return best
