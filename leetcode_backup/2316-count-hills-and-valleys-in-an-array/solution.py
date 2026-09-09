class Solution(object):
    def countHillValley(self, nums):
        count = 0
        n = len(nums)
        i = 1
        while i < n - 1:
            if nums[i] == nums[i - 1]:
                i += 1
                continue

            j = i + 1
            while j < n and nums[j] == nums[i]:
                j += 1

            if j < n:
                if (nums[i] > nums[i - 1] and nums[i] > nums[j]) or (
                    nums[i] < nums[i - 1] and nums[i] < nums[j]
                ):
                    count += 1
            i = j
        return count


# Example usage
sol = Solution()
print(sol.countHillValley([2, 4, 1, 1, 6, 5]))  # Output: 3
print(sol.countHillValley([6, 6, 5, 5, 4, 1]))  # Output: 0
