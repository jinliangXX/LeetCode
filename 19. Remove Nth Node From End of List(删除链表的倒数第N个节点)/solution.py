# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None
        left, right = head, head
        for i in range(n):
            right = right.next
        if not right:
            return head.next
        while right.next:
            right = right.next
            left = left.next
        dele = left.next
        left.next = dele.next
        return head
