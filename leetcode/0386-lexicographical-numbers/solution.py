class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = [0] * n  # preallocate
        cur = 1
        i = 0

        while i < n:
            result[i] = cur
            i += 1

            if cur * 10 <= n:
                cur *= 10
            else:
                while cur % 10 == 9 or cur + 1 > n:
                    cur //= 10
                cur += 1

        return result
