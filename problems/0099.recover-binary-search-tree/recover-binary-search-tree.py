# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        inorder_t = []
        def inorder_traversal(node, inorder_t):
            if node.left:
                inorder_traversal(node.left, inorder_t)
            inorder_t.append(node)
            if node.right:
                inorder_traversal(node.right, inorder_t)
        inorder_traversal(root, inorder_t)
        left, right = None, None
        for i in range(len(inorder_t)):
            if i < len(inorder_t)-1 and inorder_t[i].val > inorder_t[i+1].val\
                    and left is None:
                left = i
            if i > 0 and inorder_t[i].val < inorder_t[i-1].val:
                right = i
        print(left, right)
        inorder_t[left].val, inorder_t[right].val = inorder_t[right].val, inorder_t[left].val



# [1,3,null,null,2] [3,1,4,null,null,2]
t = TreeNode(1)
t.left = TreeNode(3)
t.left.right = TreeNode(2)
Solution().recoverTree(t)
print(t.val, t.left.val)