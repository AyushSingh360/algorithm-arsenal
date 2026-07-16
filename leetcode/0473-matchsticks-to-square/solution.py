from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        # Quick feasibility check
        if total % 4 != 0:
            return False

        side = total // 4

        # If any stick is longer than side, impossible
        if max(matchsticks) > side:
            return False

        # Sort in descending order to improve pruning
        matchsticks.sort(reverse=True)

        sides = [0, 0, 0, 0]

        def dfs(i: int) -> bool:
            # All sticks placed successfully
            if i == len(matchsticks):
                # Because we never exceed 'side', reaching here implies
                # all sides == side
                return sides[0] == side and sides[1] == side and sides[2] == side and sides[3] == side

            length = matchsticks[i]

            for k in range(4):
                # Try putting current stick on side k if it fits
                if sides[k] + length <= side:
                    sides[k] += length
                    if dfs(i + 1):
                        return True
                    sides[k] -= length  # backtrack

                    # Pruning: if this side was 0 before trying and still
                    # doesn't work, no need to try other empty sides
                    if sides[k] == 0:
                        break

            return False

        return dfs(0)
