from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def find_sum(node, sum, current_nums, res):
            if not node:
                return
            elif not node.left and not node.right:
                if node.val == sum:
                    res.append(current_nums + [node.val])
                return
            else:
                find_sum(node.left, sum-node.val, current_nums + [node.val],
                         res)
                find_sum(node.right, sum-node.val, current_nums + [node.val],
                         res)
        res = []
        find_sum(root, sum, [], res)
        return res