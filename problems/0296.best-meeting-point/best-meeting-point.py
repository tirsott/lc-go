from typing import List

class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        x = []
        y = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    x.append(i)
                    y.append(j)
        y.sort()
        x_mid = x[len(x)//2]
        y_mid = y[len(y)//2]
        return sum([abs(i-x_mid) for i in x]) + sum([abs(i-y_mid) for i in y])


# 输入:
#
# 1 - 0 - 0 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
#
# 输出: 6
#
# 解析: 给定的三个人分别住在(0,0)，(0,4) 和 (2,2):
#      (0,2) 是一个最佳的碰面点，其总行走距离为 2 + 2 + 2 = 6，最小，因此返回 6。
#
