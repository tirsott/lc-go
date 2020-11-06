from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        res = []
        def dfs(root, target):
            if not root:
                return
            else:
                if len(res) < k:
                    res.append(root.val)
                    res.sort()
                else:
                    if abs(root.val - target) > abs(res[0] - target) and\
                        abs(root.val - target) > abs(res[-1] - target):
                        pass
                    elif abs(res[0] - target) > abs(res[-1] - target):
                        res.pop(0)
                        res.append(root.val)
                        res.sort()
                    else:
                        res.pop(-1)
                        res.append(root.val)
                        res.sort()
                dfs(root.left, target)
                dfs(root.right, target)
        dfs(root, target)
        return res

print(Solution().closestKValues(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(
    3)), TreeNode(5)), 3.7, 2))


#
#
# 示例：
#
# 输入: root = [4,2,5,1,3]，目标值 = 3.714286，且 k = 2
#
#     4
#    / \
#   2   5
#  / \
# 1   3
#
# 输出: [4,3]
#[2,0,33,null,1,25,40,null,null,11,31,34,45,10,18,29,32,null,36,43,46,4,null,12,24,26,30,null,null,35,39,42,44,null,48,3,9,null,14,22,null,null,27,null,null,null,null,38,null,41,null,null,null,47,49,null,null,5,null,13,15,21,23,null,28,37,null,null,null,null,null,null,null,null,8,null,null,null,17,19,null,null,null,null,null,null,null,7,null,16,null,null,20,6]
# 2.428571
# 14
# 1 2 10 11 18 25 29 31 32 33 34 36 40  45
