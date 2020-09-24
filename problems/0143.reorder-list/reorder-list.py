# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        fast, slow = head, head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        l2 = slow.next
        l1 = head
        slow.next = None
        l2 = self.reserve(l2)
        while l2:
            l2_head = l2
            l2 = l2.next
            l2_head.next = l1.next
            l1.next = l2_head
            l1 = l1.next.next

    def reserve(self, head):
        l = head
        new_head = head
        while l.next:
            temp = l.next
            l.next = l.next.next
            temp.next = new_head
            new_head = temp
        return new_head

# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
Solution().reorderList(l)
while(l):
    print(l.val)
    l = l.next