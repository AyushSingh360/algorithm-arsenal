from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        def rotate(m: List[List[int]]) -> List[List[int]]:
            # 90 degrees clockwise rotation [web:16]
            return [[m[n - j - 1][i] for j in range(n)] for i in range(n)]

        for _ in range(4):
            if mat == target:
                return True
            mat = rotate(mat)

        return False
