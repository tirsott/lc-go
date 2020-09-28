from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        if k >= len(prices) // 2:
            return self.maxProfitUnlimit(prices)
        dp = [[[None for _ in range(k+1)], [None for _ in range(k+1)]] for _ in range(
            len(prices))]
        for i in range(k+1):
            dp[0][0][i] = 0
            dp[0][1][i] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0][0] = 0
            for j in range(k+1):
                if j == 0:
                    dp[i][0][j] = 0
                else:
                    dp[i][0][j] = max(dp[i-1][0][j], dp[i-1][1][j-1] + prices[i])
                if j == k:
                    dp[i][1][j] = 0
                else:
                    dp[i][1][j] = max(dp[i-1][1][j], dp[i-1][0][j] - prices[i])
        return max(dp[-1][0])

    def maxProfitUnlimit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
               res += (prices[i] - prices[i-1])
        return res

# 输入: [3,2,6,5,0,3], k = 2
# 输出: 7
# 解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
#      随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
#
import time
t = time.time()
print(Solution().maxProfit(10000, [3,2,6,5,0,3],
))
print(time.time()-t)