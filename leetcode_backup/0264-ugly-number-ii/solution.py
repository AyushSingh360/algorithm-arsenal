class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [0] * n
        ugly[0] = 1  # first ugly number

        i2 = i3 = i5 = 0  # pointers for 2, 3, 5
        next2, next3, next5 = 2, 3, 5

        for i in range(1, n):
            nxt = min(next2, next3, next5)
            ugly[i] = nxt

            if nxt == next2:
                i2 += 1
                next2 = ugly[i2] * 2
            if nxt == next3:
                i3 += 1
                next3 = ugly[i3] * 3
            if nxt == next5:
                i5 += 1
                next5 = ugly[i5] * 5

        return ugly[-1]
