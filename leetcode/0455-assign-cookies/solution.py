from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Sort greed factors and cookie sizes
        g.sort()
        s.sort()

        child = 0  # index for children (in g)
        cookie = 0  # index for cookies (in s)

        # Try to satisfy children from least greedy upwards
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                # This cookie can satisfy this child
                child += 1
                cookie += 1
            else:
                # Cookie too small, try next larger cookie
                cookie += 1

        # 'child' is the number of children satisfied
        return child
