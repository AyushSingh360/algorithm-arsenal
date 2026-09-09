class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # If start is blocked, no paths
        if obstacleGrid[0][0] == 1:
            return 0

        dp = [0] * n
        dp[0] = 1  # start cell

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0  # cannot stand on obstacle
                else:
                    if j > 0:
                        dp[j] += dp[j - 1]  # from left + from top (already in dp[j])
        return dp[-1]
