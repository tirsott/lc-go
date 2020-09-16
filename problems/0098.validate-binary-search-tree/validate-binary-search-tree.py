# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        inorder_t = []
        def inorder_traversal(node, inorder_t):
            if node.left:
                inorder_traversal(node.left, inorder_t)
            inorder_t.append(node.val)
            if node.right:
                inorder_traversal(node.right, inorder_t)
        inorder_traversal(root, inorder_t)
        for i in range(len(inorder_t)-1):
            if inorder_t[i] >= inorder_t[i+1]:
                return False
        return True

t1 = TreeNode(2)
t1.left = TreeNode(1)
t1.right = TreeNode(3)
print(Solution().isValidBST(t1))