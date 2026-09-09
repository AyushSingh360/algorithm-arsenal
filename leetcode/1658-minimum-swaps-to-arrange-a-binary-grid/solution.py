class Solution(object):
    def minSwaps(self, grid):
        n = len(grid)

        # Count trailing zeros for each row
        trailing_zeros = []
        for row in grid:
            count = 0
            for i in range(n - 1, -1, -1):
                if row[i] == 0:
                    count += 1
                else:
                    break
            trailing_zeros.append(count)

        swaps = 0

        # For each row i, we need at least (n - 1 - i) trailing zeros
        for i in range(n):
            needed = n - 1 - i

            # Find the first row from position i onwards that has enough trailing zeros
            found = -1
            for j in range(i, n):
                if trailing_zeros[j] >= needed:
                    found = j
                    break

            # If no valid row found, return -1
            if found == -1:
                return -1

            # Swap the row at position 'found' up to position 'i'
            # This takes (found - i) adjacent swaps
            swaps += found - i

            # Bubble the row up by swapping adjacent elements
            for j in range(found, i, -1):
                trailing_zeros[j], trailing_zeros[j - 1] = (
                    trailing_zeros[j - 1],
                    trailing_zeros[j],
                )

        return swaps
