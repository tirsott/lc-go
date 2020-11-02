# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0
        if self.is_unival_subtree(root):
            return self.count_node(root)
        else:
            return self.countUnivalSubtrees(root.left) + \
                   self.countUnivalSubtrees(root.right)


    def count_node(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return 1 + self.count_node(root.left) + self.count_node(root.right)


    def is_unival_subtree(self, root):
        if not root.left and not root.right:
            return True
        elif not root.left:
            return root.val == root.right.val and self.is_unival_subtree(
                root.right)
        elif not root.right:
            return root.val == root.left.val and self.is_unival_subtree(
                root.left)
        else:
            return root.val == root.left.val and root.val == root.right.val and self.is_unival_subtree(
                root.right) and self.is_unival_subtree(root.left)

print(Solution().countUnivalSubtrees(TreeNode(5, TreeNode(1, TreeNode(5), TreeNode(
    5)), TreeNode(5, None, TreeNode(5)))))

# 输入: root = [5,1,5,5,5,null,5]
#
#               5
#              / \
#             1   5
#            / \   \
#           5   5   5
#
# 输出: 4
