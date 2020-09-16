from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        def generate(start, end):
            if start > end:
                return [None]
            res = []
            for i in range(start, end+1):
                left_trees = generate(start, i-1)
                right_trees = generate(i+1, end)
                for left_tree in left_trees:
                    for right_tree in right_trees:
                        tree = TreeNode(i)
                        tree.left = left_tree
                        tree.right = right_tree
                        res.append(tree)
            return res

        return generate(1, n) if n else []

print(Solution().generateTrees(3))