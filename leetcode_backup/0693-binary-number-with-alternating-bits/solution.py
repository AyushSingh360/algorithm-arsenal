class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n <= 0:
            return False
        last_bit = n & 1
        n = n >> 1
        while n > 0:
            current_bit = n & 1
            if current_bit == last_bit:
                return False
            last_bit = current_bit
            n = n >> 1
        return True
