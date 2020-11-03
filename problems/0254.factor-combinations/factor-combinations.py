from typing import List
import math

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:

        def dfs(start, num):
            if num == 1:
                return []
            qnum = int(math.sqrt(num))
            result = []
            for i in range(start, qnum+1):
                if num % i == 0:
                    result.append([i, num//i])
                    next_lists = dfs(i, num // i)
                    for l in next_lists:
                        l.append(i)
                        result.append(l)
            return result
        return dfs(2, n)

print(Solution().getFactors(12))



# 示例 1：
#
# 输入: 1
# 输出: []
#
# 示例 2：
#
# 输入: 37
# 输出: []
#
# 示例 3：
#
# 输入: 12
# 输出:
# [
#   [2, 6],
#   [2, 2, 3],
#   [3, 4]
# ]
#
# 示例 4:
#
# 输入: 32
# 输出:
# [
#   [2, 16],
#   [2, 2, 8],
#   [2, 2, 2, 4],
#   [2, 2, 2, 2, 2],
#   [2, 4, 4],
#   [4, 8]
# ]
# 1, 2, 3 [1] [2] [3] [1,2][3] [1,3][2] [1][2,3]