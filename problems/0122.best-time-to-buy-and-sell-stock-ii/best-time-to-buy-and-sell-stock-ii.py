from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
               res += (prices[i] - prices[i-1])
        return res


print(Solution().maxProfit([7,1,5,3,6,4]))
# [7,1,5,3,6,4]