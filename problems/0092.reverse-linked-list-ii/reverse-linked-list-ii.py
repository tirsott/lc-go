# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        new_head = ListNode(-1)
        new_head.next = head
        dummy = new_head
        for i in range(m-1):
            dummy = dummy.next
        end = dummy.next
        for j in range(n-m):
            temp = dummy
            for i in range(j + 2):
                temp = temp.next
            start = dummy.next
            dummy.next = temp
            end.next = temp.next
            temp.next = start
        return new_head.next


l = [0 for i in range(5)]
for i in range(5):
    l[i] = ListNode(i+1)
for i in range(4):
    l[i].next = l[i+1]
ll = Solution().reverseBetween(l[0], 2, 4)
while ll:
    print(ll.val)
    ll = ll.next



# 1->2->3->4->5->NULL, m = 2, n = 4