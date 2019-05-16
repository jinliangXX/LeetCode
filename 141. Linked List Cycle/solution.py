# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        one = head
        two = head.next
        while two is not None and two.next is not None:
            if two is one:
                return True
            one = one.next
            two = two.next.next
        return False
