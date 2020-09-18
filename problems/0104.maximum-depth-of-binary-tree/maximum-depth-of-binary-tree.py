# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# [3,9,20,null,null,15,7]，
t = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15),
                                                 right=TreeNode(7)))
print(Solution().maxDepth(t))