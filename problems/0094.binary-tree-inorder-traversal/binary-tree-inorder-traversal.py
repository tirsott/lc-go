from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        def inorder_traversal(node, res):
            if node.left:
                inorder_traversal(node.left, res)
            res.append(node.val)
            if node.right:
                inorder_traversal(node.right, res)
        res = []
        inorder_traversal(root, res)
        return res