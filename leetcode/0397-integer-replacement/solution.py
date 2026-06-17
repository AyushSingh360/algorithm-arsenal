class Solution:
    def integerReplacement(self, n: int) -> int:
        ans = 0
        while n != 1:
            if (n & 1) == 0:       # n is even
                n >>= 1
            elif n != 3 and (n & 3) == 3:  # n ends in binary 11 and n != 3
                n += 1
            else:                    # n ends in binary 01 or n == 3
                n -= 1
            ans += 1
        return ans
