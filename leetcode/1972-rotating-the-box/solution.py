class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        # Result is n x m after 90° clockwise rotation
        ans = [["."] * m for _ in range(n)]

        for i in range(m):
            # rightmost position where a stone can fall in this row
            empty = n - 1
            # process from right to left (direction of gravity before rotation)
            for j in range(n - 1, -1, -1):
                if boxGrid[i][j] == "*":
                    # obstacle stays; also reset empty just left of obstacle
                    ans[j][m - 1 - i] = "*"
                    empty = j - 1
                elif boxGrid[i][j] == "#":
                    # place stone at the current available empty position
                    ans[empty][m - 1 - i] = "#"
                    empty -= 1
                # '.' is already handled as default in ans

        return ans
