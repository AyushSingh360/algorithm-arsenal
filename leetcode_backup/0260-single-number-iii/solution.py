class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Step 1: XOR of all numbers = a ^ b (where a and b are the two unique numbers)
        xors = 0
        for x in nums:
            xors ^= x

        # Step 2: Get a distinguishing bit (rightmost set bit in xors)
        # This bit is 1 in exactly one of (a, b) and 0 in the other
        diff_bit = xors & -xors

        # Step 3: Partition numbers into two groups based on diff_bit
        # and XOR within each group to recover a and b
        a = 0
        b = 0
        for x in nums:
            if x & diff_bit:
                a ^= x
            else:
                b ^= x

        return [a, b]
