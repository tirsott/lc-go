# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        temp = root
        while temp:
            if temp.left:
                self.get_rightest(temp.left).right = temp.right
                temp.right = temp.left
                temp.left = None
            temp = temp.right
        return

    def get_rightest(self, root):
        if not root.left and not root.right:
            return root
        if not root.right:
            return self.get_rightest(root.left)
        if not root.left:
            return self.get_rightest(root.right)
        return self.get_rightest(root.right)

a = Solution().flatten(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)),
                                            TreeNode(5, None, TreeNode(6))))
print(a.right.right.right.val)
'''
例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6

将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
'''