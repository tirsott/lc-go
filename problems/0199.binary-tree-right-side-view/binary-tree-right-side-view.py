from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        next = [root]
        while next:
            res.append(next[-1].val)
            temp = []
            for node in next:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            next = temp
        return res