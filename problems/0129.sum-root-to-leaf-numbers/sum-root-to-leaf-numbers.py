# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        num_list = []
        def dfs(node, exist_nums, num_list):
            if not node and not exist_nums:
                return
            if not node.left and not node.right:
                num_list.append(exist_nums + [node.val])
                return
            if node.left:
                dfs(node.left, exist_nums+[node.val], num_list)
            if node.right:
                dfs(node.right, exist_nums+[node.val], num_list)
        dfs(root, [], num_list)
        res = 0
        for nums in num_list:
            for i in range(len(nums)):
                res += nums[i] * (10 ** (len(nums)-1-i))
        return res


# [4,9,0,5,1]
t = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
print(Solution().sumNumbers(t))