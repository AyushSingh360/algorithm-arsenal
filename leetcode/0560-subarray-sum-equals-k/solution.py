class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Use prefix sum + hashmap approach
        # For each position, check if (current_sum - k) exists in map
        # If it does, we found subarrays that sum to k

        count = 0
        prefix_sum = 0
        sum_map = {0: 1}  # Initialize with 0:1 to handle subarrays from start

        for num in nums:
            prefix_sum += num
            # If (prefix_sum - k) exists, add its frequency to count
            if (prefix_sum - k) in sum_map:
                count += sum_map[prefix_sum - k]
            # Add current prefix_sum to map
            sum_map[prefix_sum] = sum_map.get(prefix_sum, 0) + 1

        return count
