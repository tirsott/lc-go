class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        t2, t3, t5 = 0, 0, 0
        for i in range(n-1):
            res.append(min(res[t2] * 2, res[t3]*3, res[t5]*5))
            if res[-1] == res[t2] * 2:
                t2 += 1
            if res[-1] == res[t3] * 3:
                t3 += 1
            if res[-1] == res[t5] * 5:
                t5 += 1
        return res[-1]


print(Solution().nthUglyNumber(10))





# 示例:
#
# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
# [0 0 0] [1 0 0] [0 1 0] [2 0 0] [0 0 1] [1 1 0] [3 0 0] [0 2 0] [1 0 1] [2 1 0]