from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_self_dividing(num: int) -> bool:
            x = num
            while x > 0:
                d = x % 10
                if d == 0 or num % d != 0:
                    return False
                x //= 10
            return True

        ans = []
        for n in range(left, right + 1):
            if is_self_dividing(n):
                ans.append(n)
        return ans
