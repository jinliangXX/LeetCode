# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num_next = 0
        l3 = ListNode(0)
        l3_now = l3
        while l1 is not None or l2 is not None or num_next > 0:
            if l1 is None:
                l1 = ListNode(0)
            if l2 is None:
                l2 = ListNode(0)
            now = l1.val + l2.val + num_next
            l3_now.next = ListNode(now % 10)
            l3_now = l3_now.next
            num_next = int(now / 10)
            l1 = l1.next
            l2 = l2.next
        return l3.next



