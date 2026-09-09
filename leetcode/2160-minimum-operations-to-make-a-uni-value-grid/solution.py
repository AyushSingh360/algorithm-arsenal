from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Flatten the grid into a 1D list
        arr = [val for row in grid for val in row]

        # Check feasibility: all elements must have the same remainder modulo x
        rem = arr[0] % x
        for v in arr:
            if v % x != rem:
                return -1

        # Sort to find median
        arr.sort()
        n = len(arr)
        median = arr[n // 2]

        # Sum operations: each step changes value by x
        ops = 0
        for v in arr:
            ops += abs(v - median) // x

        return ops
