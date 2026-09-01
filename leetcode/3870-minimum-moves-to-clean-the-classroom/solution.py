from collections import deque
from typing import List


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        start = None
        litter_id = {}
        k = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == "S":
                    start = (r, c)
                elif classroom[r][c] == "L":
                    litter_id[(r, c)] = k
                    k += 1

        full_mask = (1 << k) - 1
        if full_mask == 0:
            return 0

        # best[r][c][mask] = greatest remaining energy seen at this state.
        best = [[[-1] * (1 << k) for _ in range(n)] for _ in range(m)]

        sr, sc = start
        q = deque([(sr, sc, 0, energy, 0)])
        best[sr][sc][0] = energy

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while q:
            r, c, mask, remaining, moves = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                if classroom[nr][nc] == "X":
                    continue
                if remaining == 0:
                    continue

                next_energy = remaining - 1
                next_mask = mask

                if (nr, nc) in litter_id:
                    next_mask |= 1 << litter_id[(nr, nc)]

                # Reaching R restores energy immediately.
                if classroom[nr][nc] == "R":
                    next_energy = energy

                if next_mask == full_mask:
                    return moves + 1

                # Same position + litter set with more energy dominates this state.
                if next_energy <= best[nr][nc][next_mask]:
                    continue

                best[nr][nc][next_mask] = next_energy
                q.append((nr, nc, next_mask, next_energy, moves + 1))

        return -1
