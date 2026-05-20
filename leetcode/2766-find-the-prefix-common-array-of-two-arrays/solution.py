from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        # Since A and B are permutations of [1..n], we can use a size n+1 array
        freq = [0] * (n + 1)
        common = 0
        res = [0] * n

        for i in range(n):
            # Increment count for A[i]
            freq[A[i]] += 1
            if freq[A[i]] == 2:
                # This value has now appeared in both A and B's prefixes
                common += 1

            # Increment count for B[i]
            freq[B[i]] += 1
            if freq[B[i]] == 2:
                common += 1

            res[i] = common

        return res
