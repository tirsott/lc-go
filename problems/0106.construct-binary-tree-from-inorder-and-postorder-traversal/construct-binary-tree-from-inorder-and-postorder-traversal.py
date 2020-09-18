from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder or not inorder:
            return None
        root = TreeNode(postorder[-1])
        index = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index+1:], postorder[index:-1])
        return root



#中序遍历 inorder = [9,3,15,20,7]
#后序遍历 postorder = [9,15,7,20,3]
print(Solution().buildTree([9,3,15,20,7], [9,15,7,20,3]).val)