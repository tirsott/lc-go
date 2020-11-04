class Solution:
    def isUgly(self, num: int) -> bool:
        while num > 1:
            while num % 30 == 0:
                num //= 30
            while num % 6 == 0:
                num //= 6
            while num % 10 == 0:
                num //= 10
            while num % 15 == 0:
                num //= 15
            while num % 2 == 0:
                num //= 2
            while num % 3 == 0:
                num //= 3
            while num % 5 == 0:
                num //= 5
            break
        return num == 1

print(Solution().isUgly(14))




# 示例 1:
#
# 输入: 6
# 输出: true
# 解释: 6 = 2 × 3
#
# 示例 2:
#
# 输入: 8
# 输出: true
# 解释: 8 = 2 × 2 × 2
#
# 示例 3:
#
# 输入: 14
# 输出: false
# 解释: 14 不是丑数，因为它包含了另外一个质因数 7。
