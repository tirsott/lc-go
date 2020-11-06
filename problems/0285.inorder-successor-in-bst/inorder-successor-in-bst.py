# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        def dfs(last, root, p):
            if not root:
                return None
            if root == p:
                if not last and not root.right:
                    return None
                elif root.right:
                    temp = root.right
                    while temp.left:
                        temp = temp.left
                    return temp
                else:
                    return last
            elif root.val > p.val:
                return dfs(root, root.left, p)
            else:
                if root.right and root.right.val > p.val:
                    return dfs(root.right, root.right, p)
                else:
                    return dfs(last, root.right, p)
        return dfs(None, root, p)

# [6,2,8,0,4,7,9,null,null,3,5]
# 4

