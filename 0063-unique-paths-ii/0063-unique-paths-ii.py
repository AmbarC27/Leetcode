class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid[0])
        n = len(obstacleGrid)
        dp = [[0]*m for _ in range(n)]

        for i in range(m):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = 1
            else:
                break

        for j in range(n):
            if obstacleGrid[j][0] != 1:
                dp[j][0] = 1
            else:
                break

        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[j][i] == 1:
                    dp[j][i] = 0
                else:
                    dp[j][i] = dp[j-1][i] + dp[j][i-1]
        

        return dp[-1][-1]
