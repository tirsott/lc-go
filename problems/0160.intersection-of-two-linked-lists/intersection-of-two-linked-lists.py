from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        tempA = headA
        tempB = headB
        while tempA.next and tempB.next:
            if tempA == tempB:
                return tempA
            tempA = tempA.next
            tempB = tempB.next
        countA = 0
        countB = 0
        if tempA:
            while tempA.next:
                tempA = tempA.next
                countA += 1
        if tempB:
            while tempB.next:
                tempB = tempB.next
                countB += 1
        tempA = headA
        tempB = headB
        if countA:
            for i in range(countA):
                tempA = tempA.next
        if countB:
            for i in range(countB):
                tempB = tempB.next
        while tempB != tempA:
            if (not tempB or not tempA) and tempB != tempA:
                return None
            tempA = tempA.next
            tempB = tempB.next
        return tempA