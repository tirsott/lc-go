from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        dp = [[[None, None, None], [None, None, None]] for _ in range(len(prices))]
        dp[0][0][0] = 0
        dp[0][0][1] = 0
        dp[0][0][2] = 0
        dp[0][1][0] = -prices[0]
        dp[0][1][1] = -prices[0]
        dp[0][1][2] = -prices[0]
        print(dp)
        for i in range(1, len(prices)):
            dp[i][0][0] = 0
            dp[i][0][1] = max(dp[i-1][0][1], dp[i-1][1][0] + prices[i])
            dp[i][0][2] = max(dp[i-1][0][2], dp[i-1][1][1] + prices[i])
            dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][0][0] - prices[i])
            dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][1] - prices[i])
            dp[i][1][2] = 0
            print(dp)
        return max(dp[-1][0])


print(Solution().maxProfit([1,2,4,2,5,7,2,4,9,0]))

# [3,3,5,0,0,3,1,4]