from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[None for _ in range(i+1)] for i in range(len(triangle))]
        print(dp)
        for i in range(len(triangle)):
            for j in range(len(triangle[i])):
                if i == 0:
                    dp[i][j] = triangle[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    dp[i][j] = dp[i - 1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i - 1][j-1]) + triangle[i][j]
            print(dp)
        return min(dp[len(triangle)-1])



print(Solution().minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))
'''
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
'''