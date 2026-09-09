class Solution(object):
    def maxTotalFruits(self, fruits, startPos, k):
        """
        :type fruits: List[List[int]]  # each [position, amount], sorted by position
        :type startPos: int
        :type k: int
        :rtype: int
        """
        n = len(fruits)
        ans = 0
        curr_sum = 0
        l = 0

        # Helper to decide if we can collect all fruits in window [l..r]
        def window_reachable(i, j):
            left_pos = fruits[i][0]
            right_pos = fruits[j][0]
            # Case 1: all to the left of start
            if right_pos <= startPos:
                return startPos - left_pos <= k
            # Case 2: all to the right of start
            if left_pos >= startPos:
                return right_pos - startPos <= k
            # Case 3: window spans both sides
            # two possible paths: go left first, or go right first
            cost_left_first = (startPos - left_pos) * 2 + (right_pos - startPos)
            cost_right_first = (right_pos - startPos) * 2 + (startPos - left_pos)
            return min(cost_left_first, cost_right_first) <= k

        # Expand right end of window
        for r in range(n):
            curr_sum += fruits[r][1]
            # Shrink from the left until the window becomes reachable
            while l <= r and not window_reachable(l, r):
                curr_sum -= fruits[l][1]
                l += 1
            ans = max(ans, curr_sum)

        return ans
