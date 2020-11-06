import math

class Solution:
    def numSquares(self, n: int) -> int:
        # if math.sqrt(n).is_integer():
        #     return 1
        # dp = [0 for _ in range(n+1)]
        # for i in range(n+1):
        #     if math.sqrt(i).is_integer():
        #         dp[i] = 1
        #     else:
        #         dp[i] = min([dp[x]+dp[i-x] for x in range(1, i//2+1)])
        # return dp[n]
        square_nums = [i ** 2 for i in range(0, int(math.sqrt(n)) + 1)]

        dp = [float('inf')] * (n + 1)
        # bottom case
        dp[0] = 0

        for i in range(1, n + 1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)

        return dp[-1]

import time
t=time.time()
print(Solution().numSquares(5673
))
print(time.time()-t)


# 示例 1:
#
# 输入: n = 12
# 输出: 3
# 解释: 12 = 4 + 4 + 4.
#
# 示例 2:
#
# 输入: n = 13
# 输出: 2
# 解释: 13 = 4 + 9.
