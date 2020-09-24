# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast and fast == slow:
                break
            if not fast or not fast.next:
                return None
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast



# fast 2n slow n
# n = x圈 slow距离环起始位置为head到环起始位置
print(Solution().detectCycle(ListNode(1, ListNode(2))))