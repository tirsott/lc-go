# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.max_depth(root.left) - self.max_depth(root.right)) <=\
               1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def max_depth(self, root):
        if not root:
            return 0
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))

# [3,9,20,null,null,15,7]
t = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15),
                                                 right=TreeNode(7)))
print(Solution().isBalanced(t))