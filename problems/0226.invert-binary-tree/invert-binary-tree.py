# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


t = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(
    6), TreeNode(9)))
t = Solution().invertTree(t)
print(t.right.left.val)


# 输入：
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
#
# 输出：
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
