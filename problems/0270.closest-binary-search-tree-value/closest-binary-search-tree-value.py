# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        def dfs(last, target, root):
            if not root:
                return last
            if root.val == target:
                return root.val
            elif target > root.val:
                if abs(root.val - target) > abs(last - target):
                    return dfs(last, target, root.right)
                else:
                    return dfs(root.val, target, root.right)
            elif target < root.val:
                if abs(root.val - target) > abs(last - target):
                    return dfs(last, target, root.left)
                else:
                    return dfs(root.val, target, root.left)
        return dfs(root.val, target, root)

print(Solution().closestValue(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(
    3)), TreeNode(5)), 3.7))





# 示例：
#
# 输入: root = [4,2,5,1,3]，目标值 target = 3.714286
#
#     4
#    / \
#   2   5
#  / \
# 1   3
#
# 输出: 4
#