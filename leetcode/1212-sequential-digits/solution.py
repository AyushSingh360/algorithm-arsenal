from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        low_len, high_len = len(str(low)), len(str(high))

        # lengths that matter
        for length in range(low_len, high_len + 1):
            # starting digit; must leave room for 'length' digits up to 9
            for start in range(1, 10 - length + 1):
                num = 0
                # build a sequential-digit number of this length
                for i in range(length):
                    num = num * 10 + (start + i)
                if low <= num <= high:
                    res.append(num)

        res.sort()
        return res
