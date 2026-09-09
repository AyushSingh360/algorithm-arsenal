class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF  # 32 bits
        MAX_INT = 0x7FFFFFFF  # max positive 32-bit int

        # convert to 32-bit representation
        a &= MASK
        b &= MASK

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & MASK
            b = carry & MASK

        # if a is negative in 32-bit, convert from two's complement
        return a if a <= MAX_INT else ~(a ^ MASK)
