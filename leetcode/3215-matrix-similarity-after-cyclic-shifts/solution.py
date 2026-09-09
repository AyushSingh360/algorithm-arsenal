from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])

        # Shifting by n is a full cycle, so reduce k
        k %= n

        for i in range(m):
            row = mat[i]

            if i % 2 == 0:
                # even row: shifted left by k
                shifted = row[k:] + row[:k]
            else:
                # odd row: shifted right by k
                shifted = row[-k:] + row[:-k]

            if shifted != row:
                return False

        return True
