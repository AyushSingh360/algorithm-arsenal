from functools import lru_cache
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @lru_cache(None)
        def solve(expr: str) -> List[int]:
            # If it's just a number, return it
            if expr.isdigit():
                return [int(expr)]

            res = []
            # Try splitting on each operator
            for i, ch in enumerate(expr):
                if ch in "+-*":
                    left_vals = solve(expr[:i])
                    right_vals = solve(expr[i + 1 :])

                    for a in left_vals:
                        for b in right_vals:
                            if ch == "+":
                                res.append(a + b)
                            elif ch == "-":
                                res.append(a - b)
                            else:  # ch == '*'
                                res.append(a * b)
            return res

        return solve(expression)
