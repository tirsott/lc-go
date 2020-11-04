from typing import List

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        n = len(costs)
        k = len(costs[0])
        dp = [[0 for _ in range(k)] for _ in range(n)]
        dp[0] = costs[0]
        for i in range(1, n):
            for j in range(k):
                dp[i][j] = costs[i][j] + min(dp[i-1][:j]+dp[i-1][j+1:])
        return min(dp[-1])

print(Solution().minCostII([[1,5,3],[2,9,4]]))

# 示例：
#
# 输入: [[1,5,3],[2,9,4]]
# 输出: 5
# 解释: 将 0 号房子粉刷成 0 号颜色，1 号房子粉刷成 2 号颜色。最少花费: 1 + 4 = 5;
#      或者将 0 号房子粉刷成 2 号颜色，1 号房子粉刷成 0 号颜色。最少花费: 3 + 2 = 5.
#
