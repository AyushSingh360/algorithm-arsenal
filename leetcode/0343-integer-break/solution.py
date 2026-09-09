class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        # Divide n by 3 to get count of 3s and remainder
        quotient, remainder = divmod(n, 3)

        if remainder == 0:
            return 3**quotient
        elif remainder == 1:
            # Combine one 3 with remainder 1 to make 4 (3×1 < 2×2) [web:20][web:21]
            return 3 ** (quotient - 1) * 4
        else:  # remainder == 2
            return 3**quotient * 2
