# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 1
        def dfs(node, exists):
            nonlocal res
            res = max(res, exists)
            if not node:
                return
            if node.left:
                if node.val + 1 == node.left.val:
                    dfs(node.left, exists+1)
                else:
                    dfs(node.left, 1)
            if node.right:
                if node.val + 1 == node.right.val:
                    dfs(node.right, exists+1)
                else:
                    dfs(node.right, 1)
        dfs(root, 1)
        return res

t = TreeNode(2, None, TreeNode(3, TreeNode(2, TreeNode(1))))
print(Solution().longestConsecutive(t))