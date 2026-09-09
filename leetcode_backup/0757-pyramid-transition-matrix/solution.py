from typing import List
from collections import defaultdict


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # Map pair -> list of possible tops
        trans = defaultdict(list)
        for s in allowed:
            trans[(s[0], s[1])].append(s[2])

        memo = {}

        def can_build(row: str) -> bool:
            # If we reached the top (single block), success
            if len(row) == 1:
                return True

            if row in memo:
                return memo[row]

            # Generate all possible next rows and DFS
            res = self.build_next_rows(row, trans, 0, [], memo)
            memo[row] = res
            return res

        return can_build(bottom)

    def build_next_rows(self, row: str, trans, idx: int, cur: List[str], memo) -> bool:
        # If we've constructed a whole next row, recurse to build above it
        if idx == len(row) - 1:
            next_row = "".join(cur)
            # can_build is not a method here, so we cannot call self.can_build directly
            # Instead, we store and check using a DFS wrapper in the main function
            return self._dfs(next_row, trans, memo)

        a, b = row[idx], row[idx + 1]
        if (a, b) not in trans:
            return False

        # Try all possible tops for this pair
        for c in trans[(a, b)]:
            cur.append(c)
            if self.build_next_rows(row, trans, idx + 1, cur, memo):
                cur.pop()
                return True
            cur.pop()

        return False

    def _dfs(self, row: str, trans, memo) -> bool:
        if len(row) == 1:
            return True
        if row in memo:
            return memo[row]

        if self.build_next_rows(row, trans, 0, [], memo):
            memo[row] = True
        else:
            memo[row] = False
        return memo[row]
