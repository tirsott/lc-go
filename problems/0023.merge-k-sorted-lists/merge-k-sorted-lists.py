# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from typing import List

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        while len(lists) > 1:
            res = []
            for i in range(((len(lists)+1) // 2)):
                if 2 * i + 1 < len(lists):
                    res.append(self.mergeTwoLists(lists[2 * i], lists[2 * i + 1]))
                else:
                    res.append(lists[2 * i])
            lists = res
            res = []
        return lists[0]



    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        dummy = head
        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                dummy = dummy.next
                l1 = l1.next
            else:
                dummy.next = l2
                dummy = dummy.next
                l2 = l2.next
        if l1:
            dummy.next = l1
        if l2:
            dummy.next = l2
        return head.next

if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    l3 = ListNode(2)
    l3.next = ListNode(6)
    print(Solution().mergeKLists([l1,l2,l3]))