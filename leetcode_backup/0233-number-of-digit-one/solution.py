class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0

        count = 0
        base = 1  # 1, 10, 100, ...

        while base <= n:
            high = n // (base * 10)
            cur = (n // base) % 10
            low = n % base

            if cur == 0:
                count += high * base
            elif cur == 1:
                count += high * base + (low + 1)
            else:  # cur >= 2
                count += (high + 1) * base

            base *= 10

        return count
