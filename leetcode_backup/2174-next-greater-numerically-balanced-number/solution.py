from typing import List


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def is_balanced(x: int) -> bool:
            cnt = [0] * 10
            t = x
            while t > 0:
                t, d = divmod(t, 10)
                cnt[d] += 1
            # A number is numerically balanced if for every digit d used,
            # its count equals d.
            for d in range(10):
                if cnt[d] != 0 and cnt[d] != d:
                    return False
            return True

        x = n + 1
        while True:
            if is_balanced(x):
                return x
            x += 1
