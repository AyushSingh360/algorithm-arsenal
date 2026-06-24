class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        def same(x, y, size):
            first = grid[x][y]
            for i in range(x, x + size):
                for j in range(y, y + size):
                    if grid[i][j] != first:
                        return False
            return True

        def build(x, y, size):
            if same(x, y, size):
                return Node(bool(grid[x][y]), True, None, None, None, None)

            half = size // 2
            return Node(
                True, False,
                build(x, y, half),
                build(x, y + half, half),
                build(x + half, y, half),
                build(x + half, y + half, half)
            )

        return build(0, 0, n)
