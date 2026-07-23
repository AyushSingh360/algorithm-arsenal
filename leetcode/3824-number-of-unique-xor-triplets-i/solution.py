from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)

        # Special small cases
        if n == 1:
            # Only triplet is (nums[0], nums[0], nums[0]) → x ^ x ^ x = x
            return 1
        if n == 2:
            # nums is a permutation of [1, 2]
            # Possible XORs: 1, 2 only (cannot get 0 or 3)
            return 2

        # For n >= 3, we can generate all values in [0, 2^k - 1]
        # where k is the number of bits needed to represent n.
        # That is, let k = floor(log2(n)) + 1, then answer = 2^k.

        # Find most significant bit position
        k = n.bit_length()  # number of bits to represent n
        return 1 << k  # 2^k
