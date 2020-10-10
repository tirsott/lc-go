# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        old_head = head
        while head.next:
            new_head = head.next
            head.next = new_head.next
            new_head.next = old_head
            old_head = new_head
        return new_head



# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
l2 = Solution().reverseList(l1)
while l2:
    print(l2.val)
    l2 = l2.next