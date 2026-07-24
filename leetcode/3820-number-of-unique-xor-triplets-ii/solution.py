class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        # Set of all pairwise XORs: nums[i] ^ nums[j] for i < j
        pairs = set()
        for i in range(n):
            for j in range(i + 1, n):
                pairs.add(nums[i] ^ nums[j])

        # Use a set instead of BitSet; in Python this is simpler and efficient enough
        triplets = set()
        for pair in pairs:
            for num in nums:
                triplets.add(pair ^ num)

        return len(triplets)
