# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = TreeNode(-1)
        self.root.right = root
        self.temp = self.root

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.root.right.left:
            left = self.root.right
            while left.left and left.left.left:
                left = left.left
            num = left.left.val
            left.left = left.left.right
            self.root = self.temp
        else:
            num = self.root.right.val
            self.root.right = self.root.right.right
        return num




    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return True if self.root.right else False

# BSTIterator iterator = new BSTIterator(root);
# iterator.next();    // 返回 3
# iterator.next();    // 返回 7
# iterator.hasNext(); // 返回 true
# iterator.next();    // 返回 9
# iterator.hasNext(); // 返回 true
# iterator.next();    // 返回 15
# iterator.hasNext(); // 返回 true
# iterator.next();    // 返回 20
# iterator.hasNext(); // 返回 false

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
iterator = BSTIterator(TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9),
                                                    TreeNode(20))))
print(iterator.next())    # 返回 3
print(iterator.next() )   # 返回 7
print(iterator.hasNext()) # 返回 true
print(iterator.next())    # 返回 9
print(iterator.hasNext()) # 返回 true
print(iterator.next())    # 返回 15
print(iterator.hasNext()) # 返回 true
print(iterator.next())    # 返回 20
print(iterator.hasNext()) # 返回 false


