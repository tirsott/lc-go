from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        res = 0
        minp = prices[0]
        maxp = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < minp:
                minp = prices[i]
                maxp = prices[i]
            else:
                if prices[i] > maxp:
                    maxp = prices[i]
                    res = max(res, maxp - minp)
        return res


# [7,1,5,3,6,4]
print(Solution().maxProfit([7,1,5,3,6,4]))