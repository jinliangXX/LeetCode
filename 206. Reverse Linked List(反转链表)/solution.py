# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''

两种解答
迭代：
        if not head:
            return None
        last = None
        node = head
        while node:
            node_next = node.next
            node.next = last
            last = node
            node = node_next
        return last
        
递归：
self.root = ListNode(0)

        def get_result(node: ListNode):
            if not node:
                return self.root
            next_node = get_result(node.next)
            next_node.next = node
            return node

        ago = get_result(head)
        ago.next = None
        return self.root.next
'''


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        last = None
        node = head
        while node:
            node_next = node.next
            node.next = last
            last = node
            node = node_next
        return last


'''
        if not head:
            return head
        node = head.next
        head.next = None
        while node:
            next_node = node.next
            node.next = head
            head = node
            node = next_node
        return head
'''
'''
        def next_node(now: ListNode):
            print('*')
            if now.next:
                first, last = next_node(now.next)
                last.next = now
                now.next = None
                return first, now
            else:
                return now, now

        if not head:
            return None
        first, _ = next_node(head)
        return first
'''

if __name__ == '__main__':
    so = Solution()
    a = ListNode(1)
    a.next = ListNode(2)
    so.reverseList(a)
