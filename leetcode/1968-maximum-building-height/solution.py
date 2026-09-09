class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        # Add building 1 with fixed height 0
        restrictions.append([1, 0])

        # If there is no restriction at building n, add its natural upper bound (n - 1)
        # because you can increase by at most 1 from building 1 (height 0)
        has_n = any(r[0] == n for r in restrictions)
        if not has_n:
            restrictions.append([n, n - 1])

        # Sort by building index
        restrictions.sort(key=lambda x: x[0])

        m = len(restrictions)

        # Left-to-right pass: tighten with respect to previous restriction
        for i in range(1, m):
            idx_prev, h_prev = restrictions[i - 1]
            idx_cur, h_cur = restrictions[i]
            # Max height reachable from left: h_prev + distance
            max_from_left = h_prev + (idx_cur - idx_prev)
            restrictions[i][1] = min(h_cur, max_from_left)

        # Right-to-left pass: tighten with respect to next restriction
        for i in range(m - 2, -1, -1):
            idx_next, h_next = restrictions[i + 1]
            idx_cur, h_cur = restrictions[i]
            # Max height reachable from right: h_next + distance
            max_from_right = h_next + (idx_next - idx_cur)
            restrictions[i][1] = min(h_cur, max_from_right)

        # Compute maximum possible peak between each adjacent pair
        ans = 0
        for i in range(m - 1):
            x1, h1 = restrictions[i]
            x2, h2 = restrictions[i + 1]
            d = x2 - x1
            # Highest peak between them given |Δheight| <= 1 per building:
            # peak = (h1 + h2 + d) // 2
            peak = (h1 + h2 + d) // 2
            ans = max(ans, peak)

        return ans
