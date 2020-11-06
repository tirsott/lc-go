class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return k ** n
        else:
            dp = [[] for _ in range(n+1)]
            dp[1] = [k, 0]
            dp[2] = [k ** 2, k]
            for i in range(3, n+1):
                dp[i] = [dp[i-1][0] * k - dp[i-1][1], dp[i-1][0]-dp[i-1][1]]
        return dp[n][0]


# 示例:
#
# 输入: n = 3，k = 2
# 输出: 6
# 解析: 用 c1 表示颜色 1，c2 表示颜色 2，所有可能的涂色方案有:
#
#             柱 1    柱 2   柱 3
#  -----      -----  -----  -----
#    1         c1     c1     c2
#    2         c1     c2     c1
#    3         c1     c2     c2
#    4         c2     c1     c1
#    5         c2     c1     c2
#    6         c2     c2     c1
#
