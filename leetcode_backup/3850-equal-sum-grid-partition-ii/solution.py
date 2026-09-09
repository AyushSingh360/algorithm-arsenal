class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum(sum(row) for row in grid)
        m, n = len(grid), len(grid[0])

        def canPartition(g):
            # g is either original, reversed, transposed, or reversed-transposed
            # We iterate through rows of g. Each row is a "line" in the grid g.
            # At each step, topSum = sum of rows 0..i, botSum = sum of rows i+1..end
            # diff = topSum - botSum
            # If diff > 0: need to remove diff from top section
            # If diff < 0: need to remove -diff from bottom section
            # For the section where we remove, connectivity matters:
            # - If the section is a single line (single row in g), we can only remove
            #   corner/edge cells to keep it connected
            # - If the section has multiple lines, we can remove any cell
            prefix = 0
            seen = set()
            for i, row in enumerate(g):
                prefix += sum(row)
                suffix = total - prefix
                seen |= set(row)
                diff = prefix - suffix
                if diff == 0:
                    return True
                # Try to remove diff from prefix section (top section)
                # If diff > 0, we need to remove value = diff from prefix
                # If diff < 0, we need to remove value = -diff from suffix
                # For prefix section removal:
                # - If i == 0: prefix is just one row. Can only remove corners
                # - If i > 0 and len(g[0]) > 1: prefix has multiple rows, can remove any cell
                # Corners of the prefix section are always: g[0][0], g[0][-1], row[0]
                if diff > 0:
                    if diff in (g[0][0], g[0][-1], row[0]):
                        return True
                    if len(g[0]) > 1 and i > 0 and diff in seen:
                        return True
            return False

        # 4 orientations to check:
        # 1. grid: horizontal cuts, try removing from top
        # 2. grid[::-1]: horizontal cuts, try removing from bottom (reversed)
        # 3. transposed: vertical cuts, try removing from left
        # 4. transposed[::-1]: vertical cuts, try removing from right (reversed)
        if canPartition(grid):
            return True
        if canPartition(grid[::-1]):
            return True
        transposed = [list(row) for row in zip(*grid)]
        if canPartition(transposed):
            return True
        if canPartition(transposed[::-1]):
            return True
        return False
