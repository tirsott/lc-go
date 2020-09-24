# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        head = None
        def dfs(node):
            nonlocal head
            if not node or (not node.left and not node.right):
                if node and (head is None):
                    head = node
                return node
            left = dfs(node.left)
            right = dfs(node.right)
            if left:
                left.right = node
                left.left = right
            node.left, node.right = None, None
            return node
        dfs(root)
        return head

# 输入: [1,2,3,4,5]
#
#     1
#    / \
#   2   3
#  / \
# 4   5
#
# 输出: 返回二叉树的根 [4,5,2,#,#,3,1]
#
#    4
#   / \
#  5   2
#     / \
#    3   1
