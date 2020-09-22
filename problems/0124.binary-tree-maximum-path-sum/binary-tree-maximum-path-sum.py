# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_path(root)
        return self.max_path_sum(root)

    def max_path_sum(self, node):
        if not node:
            return 0
        if not node.left and not node.right:
            return node.val
        if not node.left:
            return max(node.val + max(node.right.maxval, 0),
                       self.max_path_sum(node.right))
        if not node.right:
            return max(node.val + max(node.left.maxval, 0),
                       self.max_path_sum(node.left))
        return max(node.val + max(node.left.maxval, 0) + max(
            node.right.maxval, 0), self.max_path_sum(node.left),
                   self.max_path_sum(node.right))

    def max_path(self, node):
        if not node:
            return 0
        if not node.left and not node.right:
            node.maxval = node.val
            return node.val
        node.maxval = max(max(self.max_path(node.left), 0),
                      max(self.max_path(node.right), 0)) + node.val
        return node.maxval

#[9,6,-3,null,null,-6,2,null,null,2,null,-6,-6,-6]
#    -10
#    / \
#   9  20
#     /  \
#    15   7
t = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
t1 = TreeNode(-2, TreeNode(-1))
a = Solution().maxPathSum(t)
print(a)
print(t.left.maxval)