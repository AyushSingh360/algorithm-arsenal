class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            # take last bit of n and add to res
            res = (res << 1) | (n & 1)
            # shift n right to process next bit
            n >>= 1
        return res
