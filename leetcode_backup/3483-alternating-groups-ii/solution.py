class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """
        n = len(colors)
        ans = cnt = 0

        # Traverse through 2n entries using modulo to simulate circular behavior
        for i in range(n * 2):
            if i > 0 and colors[i % n] == colors[(i - 1) % n]:
                cnt = 1
            else:
                cnt += 1

            # Only count when we've seen at least k and are in the second round
            if i >= n and cnt >= k:
                ans += 1

        return ans
