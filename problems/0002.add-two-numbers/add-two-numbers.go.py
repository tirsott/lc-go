
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        temp = res
        flag = 0
        while l1 and l2:
            temp.next = ListNode((l1.val + l2.val + flag) % 10)
            temp = temp.next
            flag = (l1.val + l2.val + flag) // 10
            l1 = l1.next
            l2 = l2.next
        while l1:
            temp.next = ListNode((l1.val + flag) % 10)
            temp = temp.next
            flag = (l1.val + flag) // 10
            l1 = l1.next
        while l2:
            temp.next = ListNode((l2.val + flag) % 10)
            temp = temp.next
            flag = (l2.val + flag) // 10
            l2 = l2.next
        if flag:
            temp.next = ListNode(1)
        return res.next

if __name__ == '__main__':
    a = ListNode(2)
    a.next = ListNode(4)
    a.next.next = ListNode(3)
    b = ListNode(5)
    b.next = ListNode(6)
    b.next.next = ListNode(4)
    c = Solution().addTwoNumbers(a, b)
    print(c.val, c.next.val, c.next.next.val)