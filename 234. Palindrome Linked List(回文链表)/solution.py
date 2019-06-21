# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        if not head.next.next:
            if head.val == head.next.val:
                return True
            else:
                return False

        left = head
        right = head.next.next
        while right:
            if not right.next or not right.next.next:
                break
            right = right.next.next
            left = left.next
        root = left.next
        next_node = root.next
        root.next = None
        while next_node.next:
            now = next_node.next
            next_node.next = root
            root = next_node
            next_node = now
        next_node.next = root
        while next_node.next:
            if head.val != next_node.val:
                return False
            next_node = next_node.next
            head = head.next
        return True
