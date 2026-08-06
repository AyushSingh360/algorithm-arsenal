class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        # iterate from n upwards until we find a valid number
        cur = n
        while True:
            # compute product of digits of cur
            prod = 1
            x = cur
            while x > 0:
                digit = x % 10
                prod *= digit
                x //= 10

            # check divisibility condition
            if prod % t == 0:
                return cur

            cur += 1
