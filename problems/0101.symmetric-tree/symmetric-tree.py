# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def dfs(left, right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            return left.val == right.val and dfs(left.left, right.right) and \
                   dfs(left.right, right.left)
        return dfs(root.left, root.right)


# [1,2,2,3,4,4,3]
t = TreeNode(1, left=TreeNode(2, left=TreeNode(3), right=TreeNode(4)),
                              right=TreeNode(2, left=TreeNode(4),
                                             right=TreeNode(3)))
print(Solution().isSymmetric(t))