# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        node_list = [root]
        while node_list:
            next = []
            for i in range(len(node_list)):
                if i < len(node_list) - 1:
                    node_list[i].next = node_list[i+1]
                else:
                    node_list[i].next = None
                if node_list[i].left:
                    next.append(node_list[i].left)
                if node_list[i].right:
                    next.append(node_list[i].right)
            node_list = next
        return root
