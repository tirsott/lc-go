# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.lowest(root, p, q, [], [])

    def lowest(self, root, p, q, left_val, right_val):
        if not left_val and not right_val:
            left_val, right_val = self.get_root_left_right(root)
        if p == root or q == root or (p in left_val and q in right_val) or (p
                in right_val and q in left_val):
            return root
        elif p in left_val and q in left_val:
            return self.lowest(root.left, p, q, left_val[:left_val.index(
                root.left)], left_val[left_val.index(root.left)+1:])
        else:
            return self.lowest(root.right, p, q, right_val[:right_val.index(
                root.right)], right_val[right_val.index(root.right) + 1:])


    def get_root_left_right(self, root):
        res = []
        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root)
                inorder(root.right)
        inorder(root)
        return res[:res.index(root)], res[res.index(root)+1:]


t = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(
    4))), TreeNode(1, TreeNode(0), TreeNode(8)))
print(Solution().get_root_left_right(t))


# 示例 1:
#
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
#
# 示例 2:
#
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出: 5
# 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
#
#
#                 3
#                /  \
#               5    1
#              / \   / \
#             6   2  0  8
#                /  \
#               7   4