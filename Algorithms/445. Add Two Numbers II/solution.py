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
        stack_l1 = list()
        stack_l2 = list()
        while l1 or l2:
            if l1:
                stack_l1.append(l1.val)
                l1 = l1.next
            if l2:
                stack_l2.append(l2.val)
                l2 = l2.next
        num_next = 0
        root_next = None
        while len(stack_l1) > 0 or len(
                stack_l2) > 0 or num_next != 0:
            num_l1 = 0
            num_l2 = 0
            if len(stack_l1) > 0:
                num_l1 = stack_l1.pop()
            if len(stack_l2) > 0:
                num_l2 = stack_l2.pop()
            num = num_l1 + num_l2 + num_next
            listnode = ListNode(num % 10)
            listnode.next = root_next
            root_next = listnode
            num_next = int(num / 10)
        return root_next
