from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        node_list = [root]
        while node_list:
            vals = []
            next = []
            for node in node_list:
                vals.append(node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            res.append(vals)
            node_list = next
        return res

# [3,9,20,null,null,15,7]
t = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15),
                                                 right=TreeNode(7)))
print(Solution().levelOrder(None))