# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = 0
        lenB = 0
        nowA = headA
        nowB = headB
        while nowA is not None:
            lenA += 1
            nowA = nowA.next
        while nowB is not None:
            lenB += 1
            nowB = nowB.next
        if lenA > lenB:
            for i in range(lenA - lenB):
                headA = headA.next
        else:
            for i in range(lenB - lenA):
                headB = headB.next
        while headA is not None:
            if headA is headB:
                return headA
            headA = headA.next
            headB = headB.next
