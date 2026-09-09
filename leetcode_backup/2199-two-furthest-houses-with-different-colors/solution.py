class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)

        # Farthest from the leftmost house (index 0)
        max_dist = 0
        for i in range(n - 1, -1, -1):
            if colors[i] != colors[0]:
                max_dist = max(max_dist, i)  # distance = i - 0
                break  # this is the farthest from the right

        # Farthest from the rightmost house (index n - 1)
        for i in range(n):
            if colors[i] != colors[n - 1]:
                max_dist = max(max_dist, n - 1 - i)
                break  # this is the farthest from the left

        return max_dist
