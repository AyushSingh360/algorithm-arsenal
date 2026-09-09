from typing import List


class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # prefix[j][i] = sum of grid[0..i-1][j] (i elements) for column j
        prefix = [[0] * (n + 1) for _ in range(n)]
        for j in range(n):
            for i in range(n):
                prefix[j][i + 1] = prefix[j][i] + grid[i][j]

        # prevPick[i]  = best score up to previous column,
        #                where previous column is selected and its bottommost black cell is row i-1
        # prevSkip[i]  = best score up to previous column,
        #                where previous column is skipped and the last selected column before it
        #                has bottommost black cell in row i-1
        prevPick = [0] * (n + 1)
        prevSkip = [0] * (n + 1)

        # process columns from 1 to n-1 (column 0 is the "previous" when j = 1)
        for j in range(1, n):
            currPick = [0] * (n + 1)
            currSkip = [0] * (n + 1)

            # curr = current column's chosen bottom row index (+1), 0..n
            # prev = previous chosen bottom row index (+1), 0..n
            for curr in range(n + 1):
                for prev in range(n + 1):
                    if curr > prev:
                        # current bottom is deeper than previous bottom
                        # contribution from column j-1: rows [prev, curr)
                        score = prefix[j - 1][curr] - prefix[j - 1][prev]

                        # only valid if previous column was skipped: we add contribution
                        # using prevSkip; both picking or skipping current are allowed
                        currPick[curr] = max(currPick[curr], prevSkip[prev] + score)
                        currSkip[curr] = max(currSkip[curr], prevSkip[prev] + score)
                    else:
                        # previous bottom is deeper or equal to current bottom
                        # contribution from current column j: rows [curr, prev)
                        score = prefix[j][prev] - prefix[j][curr]

                        # if we pick current, we must have picked previous (to get adjacency)
                        currPick[curr] = max(currPick[curr], prevPick[prev] + score)

                        # if we skip current, score doesn't change, but state comes from prevPick
                        currSkip[curr] = max(currSkip[curr], prevPick[prev])

            prevPick = currPick
            prevSkip = currSkip

        return max(prevPick)
