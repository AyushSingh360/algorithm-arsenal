class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [["#"] * n for _ in range(m)]
        grid[0] = ["."] * n
        for row in range(m):
            grid[row][-1] = "."
        return ["".join(row) for row in grid]
