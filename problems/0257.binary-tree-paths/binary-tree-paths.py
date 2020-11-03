from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        paths = self._get_paths(root)
        return ["->".join([str(x) for x in path]) for path in paths]

    def _get_paths(self, root):
        res = []
        def dfs(exists, root):
            if not root.left and not root.right and exists+[root.val] not in \
                    res:
                res.append(exists+[root.val])
            if root.left:
                dfs(exists+[root.val], root.left)
            if root.right:
                dfs(exists+[root.val], root.right)
        dfs([], root)
        return res


t = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
print(Solution().binaryTreePaths(t))



# 输入:
#
#    1
#  /   \
# 2     3
#  \
#   5
#
# 输出: ["1->2->5", "1->3"]
#
# 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
