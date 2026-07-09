class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # XOR gives 1 at positions where bits differ
        xor = x ^ y
        # In Python 3.8+, bit_count() returns the number of 1-bits
        return xor.bit_count()
