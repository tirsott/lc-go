from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = grid
        for i in range(1, len(grid[0])):
            dp[0][i] = dp[0][i] + dp[0][i-1]
        for i in range(1, len(grid)):
            dp[i][0] = dp[i][0] + dp[i-1][0]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + dp[i][j]
        return dp[-1][-1]



print(Solution().minPathSum([[0]]
))
