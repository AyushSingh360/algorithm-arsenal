class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        import heapq

        # Edge cases
        if not nums1 or not nums2 or k == 0:
            return []

        # Min heap: stores (sum, i, j) where i is index in nums1, j is index in nums2
        heap = []

        # Initialize heap with pairs (nums1[i], nums2[0]) for first min(k, len(nums1)) elements
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        result = []

        # Extract k smallest pairs
        while heap and len(result) < k:
            curr_sum, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])

            # If there's a next element in nums2, push the next pair with same i
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return result
