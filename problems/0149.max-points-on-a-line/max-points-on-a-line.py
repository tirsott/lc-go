from typing import List
import math

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 2:
            return len(points)
        slope = [[None for _ in range(len(points))] for _ in range(len(points))]
        res = 1
        for i in range(len(points)):
            slope[i][i] = 'any'
            for j in range(i+1, len(points)):
                if points[i] == points[j]:
                    slope[i][j] = slope[j][i] = 'any'
                    continue
                if points[i][0]-points[j][0] == 0:
                    slope[i][j] = slope[j][i] = 'max'
                    continue
                y = points[i][1]-points[j][1]
                x = points[i][0]-points[j][0]
                if x*y >0:
                    x, y = abs(x), abs(y)
                else:
                    if y<0:
                        x, y = -x, -y
                slope[i][j] = '{}/{}'.format(y/math.gcd(x, y), x/math.gcd(x, y))
                slope[j][i] = slope[i][j]
            res = max(res, self.get_max_count(slope[i]))
        return res

    def get_max_count(self, nums):
        res = 1
        key = [None]
        for num in nums:
            if num in key:
                continue
            else:
                if num != 'any':
                    res = max(nums.count(num)+nums.count('any'), res)
                else:
                    res = max(nums.count(num), res)
                key.append(num)
        return res

# 输入: [[1,1],[2,2],[3,3]]
# 输出: 3
print(Solution().maxPoints([[1,1],[2,2],[3,3]]))