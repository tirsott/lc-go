from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m == 1:
            return 0 if obstacleGrid[0].count(1) else 1
        if n == 1:
            return 0 if [x[0] for x in obstacleGrid].count(1) else 1
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 0 if obstacleGrid[0][0] else 1
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i-1][0]
        for i in range(1, n):
            if obstacleGrid[0][i] == 1:
                dp[0][i] = 0
            else:
                dp[0][i] = dp[0][i-1]
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

print(Solution().uniquePathsWithObstacles([[1,0,0,0,0,0],[0,1,0,1,0,0]]

))