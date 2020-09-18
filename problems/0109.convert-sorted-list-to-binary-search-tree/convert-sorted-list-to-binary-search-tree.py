from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return self.sortedArrayToBST(nums)

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        node = TreeNode(nums[len(nums) // 2])
        node.left = self.sortedArrayToBST(nums[:len(nums) // 2])
        node.right = self.sortedArrayToBST(nums[len(nums) // 2 + 1:])
        return node