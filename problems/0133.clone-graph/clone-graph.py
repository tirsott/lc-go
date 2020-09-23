import copy

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        clone = {}
        def dfs(node):
            if not node:
                return
            if node in clone:
                return clone[node]
            clone[node] = Node(node.val, [])
            for neighbor in node.neighbors:
                clone[node].neighbors.append(dfs(neighbor))
            return clone[node]
        return dfs(node)
