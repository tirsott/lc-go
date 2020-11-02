from typing import List
from itertools import permutations

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        num_list = []
        operator_list = []
        i = 0
        while i < len(input):
            if input[i] in '+-*':
                operator_list.append(input[i])
            else:
                start = i
                while i < len(input) - 1 and input[i+1].isdigit():
                    i += 1
                num_list.append(int(input[start:i+1]))
            i += 1
        dp = [[[] for _ in range(len(num_list))] for _ in range(len(num_list))]
        for i in range(len(num_list)):
            dp[i][i] = [num_list[i]]
        for i in range(1, len(num_list)):
            for j in range(len(num_list)):
                if i + j < len(num_list):
                    dp[j][j+i] = []
                    for x in range(i):
                        dp[j][j+i] += self.cal(operator_list[j+x],
                                               dp[j][j+x],
                                               dp[j+x+1][j+i])
        return dp[0][-1]

    def cal(self, operator, left, right):
        if operator == '+':
            return [x + y for x in left for y in right]
        elif operator == '-':
            return [x - y for x in left for y in right]
        if operator == '*':
            return [x * y for x in left for y in right]


print(Solution().diffWaysToCompute("2-1-1"))

# 示例 1:
#
# 输入: "2-1-1"
# 输出: [0, 2]
# 解释:
# ((2-1)-1) = 0
# (2-(1-1)) = 2
#
# 示例 2:
#
# 输入: "2*3-4*5"
# 输出: [-34, -14, -10, -10, 10]
# 解释:
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
