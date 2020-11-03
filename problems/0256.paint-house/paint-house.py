from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        dp = [[] for _ in range(len(costs))]
        dp[0] = costs[0]
        for i in range(1, len(costs)):
            dp[i] = [
                costs[i][0] + min(dp[i-1][1], dp[i-1][2]),
                costs[i][1] + min(dp[i-1][0], dp[i-1][2]),
                costs[i][2] + min(dp[i-1][1], dp[i-1][0]),
            ]
        return min(dp[-1])


print(Solution().minCost([[17,2,17],[16,16,5],[14,3,19]]))

# 示例：
#
# 输入: [[17,2,17],[16,16,5],[14,3,19]]
# 输出: 10
# 解释: 将 0 号房子粉刷成蓝色，1 号房子粉刷成绿色，2 号房子粉刷成蓝色。
#      最少花费: 2 + 5 + 3 = 10。
#
