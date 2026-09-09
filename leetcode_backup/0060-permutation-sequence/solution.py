from typing import List


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # make k zero-based
        k -= 1

        # precompute factorials
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i

        nums = [str(i) for i in range(1, n + 1)]
        ans = []

        for i in range(n, 0, -1):
            block_size = fact[i - 1]
            index = k // block_size
            k %= block_size

            ans.append(nums.pop(index))

        return "".join(ans)
