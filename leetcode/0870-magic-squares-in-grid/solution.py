from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if rows < 3 or cols < 3:
            return 0
        
        def is_magic(r: int, c: int) -> bool:
            # collect all 3x3 values
            nums = []
            for i in range(3):
                for j in range(3):
                    nums.append(grid[r + i][c + j])
            
            # must be 1..9 and all distinct
            if set(nums) != set(range(1, 10)):
                return False
            
            # center must be 5 (property of 3x3 normal magic squares)
            if grid[r + 1][c + 1] != 5:
                return False
            
            # check rows
            for i in range(3):
                if grid[r + i][c] + grid[r + i][c + 1] + grid[r + i][c + 2] != 15:
                    return False
            
            # check columns
            for j in range(3):
                if grid[r][c + j] + grid[r + 1][c + j] + grid[r + 2][c + j] != 15:
                    return False
            
            # check diagonals
            if grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != 15:
                return False
            if grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] != 15:
                return False
            
            return True
        
        ans = 0
        for r in range(rows - 2):
            for c in range(cols - 2):
                if is_magic(r, c):
                    ans += 1
        
        return ans
