# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        left = ListNode(-1)
        left_root = left
        right = ListNode(-1)
        right_root = right
        num = 1
        while head:
            if num % 2 == 1:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next
            num += 1
        right.next = None
        left.next = right_root.next
        return left_root.next
