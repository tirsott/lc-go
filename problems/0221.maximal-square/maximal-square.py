from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        res = 0
        for i in range(min(len(matrix), len(matrix[0]))):
            for col in range(i, len(matrix[0])):
                if i == 0:
                    dp[i][col] = 0 if matrix[i][col] == '0' else 1
                else:
                    dp[i][col] = 0 if matrix[i][col] == '0' else min(dp[i-1][col], dp[i][col-1], dp[i-1][col-1])+1
                res = max(res, dp[i][col])
            for row in range(i, len(matrix)):
                if i == 0:
                    dp[row][i] = 0 if matrix[row][i] == '0' else 1
                else:
                    dp[row][i] = 0 if matrix[row][i] == '0' else min(dp[row-1][
                                                                         i], dp[row][i-1], dp[row-1][i-1])+1
                res = max(res, dp[row][i])
        return res ** 2



# 输入:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# 输出: 4
print(Solution().maximalSquare([["1","0","1","0","0"],
                                ["1","0","1","1","1"],
                                ["1","1","1","1","1"],
                                ["1","0","0","1","0"]]))