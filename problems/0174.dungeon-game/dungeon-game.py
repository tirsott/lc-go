from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]
        row = len(dungeon)
        column = len(dungeon[0])
        dp[row-1][column-1] = 1 if dungeon[row-1][column-1] >= 0 else 1 - dungeon[row-1][column-1]
        for i in range(column-2, -1, -1):
            if dungeon[row-1][i] < dp[row - 1][i+1]:
                dp[row - 1][i] = dp[row - 1][i+1] - dungeon[row-1][i]
            else:
                dp[row - 1][i] = 1
        for i in range(row-2, -1, -1):
            if dungeon[i][column-1] < dp[i+1][column-1]:
                dp[i][column-1] = dp[i+1][column-1] - dungeon[i][column-1]
            else:
                dp[i][column-1] = 1
        for i in range(row-2, -1, -1):
            for j in range(column-2, -1, -1):
                next = min(dp[i+1][j], dp[i][j+1])
                if dungeon[i][j] < next:
                    dp[i][j] = next - dungeon[i][j]
                else:
                    dp[i][j] = 1
        return dp[0][0]



            #
# -2 (K) 	-3 	3
# -5 	-10 	1
# 10 	30 	-5 (P)
print(Solution().calculateMinimumHP([[0,0,0],[1,1,-1]]))
