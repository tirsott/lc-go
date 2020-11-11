# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = {}
        def dfs(node, order):
            if not node:
                return
            res[order] = node.val
            dfs(node.left, order*2+1)
            dfs(node.right, order*2+2)
        dfs(root, 0)
        return str(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        l = eval(data)
        for key in l:
            l[key] = TreeNode(l[key])
        for k in l:
            if k*2+1 in l:
                l[k].left = l[k*2+1]
            if k*2+2 in l:
                l[k].right = l[k*2+2]
        return l[0] if l else None

root = TreeNode(1)
node = root
for i in range(1, 1000):
    node.right = TreeNode(i+1)
    node = node.right
print()
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))