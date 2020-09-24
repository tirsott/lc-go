from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(root, res):
            if not root:
                return
            dfs(root.left, res)
            dfs(root.right, res)
            res.append(root.val)
        dfs(root, res)
        return res


t = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(Solution().postorderTraversal(t))
