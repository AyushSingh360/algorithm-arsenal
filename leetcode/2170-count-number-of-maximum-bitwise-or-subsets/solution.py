class Solution:
    def countMaxOrSubsets(self, nums):
        n = len(nums)
        max_or = 0
        count = [0]  # Use a list to make count mutable inside dfs

        # Step 1: Find the maximum OR of all numbers
        for num in nums:
            max_or |= num

        def dfs(index, current_or):
            if index == n:
                if current_or == max_or:
                    count[0] += 1
                return

            # Include current element
            dfs(index + 1, current_or | nums[index])
            # Exclude current element
            dfs(index + 1, current_or)

        # Start DFS
        dfs(0, 0)
        return count[0]
