from typing import List
import sys
sys.setrecursionlimit(100000)

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        new_min = float('-inf')  # 初始化下限值
        for i in range(len(preorder)):
            if preorder[i] < new_min: return False
            while stack and preorder[i] > stack[-1]:
                new_min = stack.pop()
            stack.append(preorder[i])
        return True

import time
t = time.time()
l = [i for i in range(1, 7998)] + [7999, 8000, 7998]
print(Solution().verifyPreorder(l))
print(time.time()-t)

#      5
#     / \
#    2   6
#   / \
#  1   3
#
# 示例 1：
#
# 输入: [5,2,6,1,3]
# 输出: false
#
# 示例 2：
#
# 输入: [5,2,1,3,6]
# 输出: true
#