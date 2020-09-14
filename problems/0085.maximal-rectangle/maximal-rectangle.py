from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        dp = [[None for _ in range(len(matrix[0]))] for _ in range(len(
            matrix))]
        dp[0][0] = (1, 1, 1) if matrix[0][0] == '1' else (0, 0, 0)
        res = max(0, dp[0][0][2])
        for i in range(1, len(matrix[0])):
            if matrix[0][i] == '1':
                dp[0][i] = (dp[0][i-1][0]+1, 1, dp[0][i-1][0]+1)
            else:
                dp[0][i] = (0, 0, 0)
            res = max(res, dp[0][i][2])
        for i in range(1, len(matrix)):
            if matrix[i][0] == '1':
                dp[i][0] = (1, dp[i-1][0][1]+1, dp[i-1][0][1]+1)
            else:
                dp[i][0] = (0, 0, 0)
            res = max(res, dp[i][0][2])
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '0':
                    dp[i][j] = (0, 0, 0)
                else:
                    left = dp[i][j-1][0] + 1
                    up = dp[i-1][j][1] + 1
                    dp[i][j] = (left, up, 0)
                    area = 0
                    for k in range(j, j-left, -1):
                        area = max(area, (j-k+1)*min([dp[i][x][1] for x in
                                                      range(j, k-1, -1)]))
                    dp[i][j] = (left, up, area)
                    res = max(res, area)
        return res


print(Solution().maximalRectangle([["0","1","1","0","1"],
                                   ["1","1","0","1","0"],
                                   ["0","1","1","1","0"],
                                   ["1","1","1","1","0"],
                                   ["1","1","1","1","1"],
                                   ["0","0","0","0","0"]]))