# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def get_list(head: ListNode, num: int):
            a = head
            for _ in range(num - 1):
                if not head:
                    return a, None, None
                head = head.next
            if not head:
                return a, None, None
            b = head.next
            head.next = None
            head = b
            for _ in range(num - 1):
                if not head:
                    return a, b, None
                head = head.next
            if not head:
                return a, b, None
            c = head.next
            head.next = None
            return a, b, c

        num = 1
        lenght = 0
        now = head
        while now:
            lenght += 1
            now = now.next
        while num < lenght:
            is_head = True
            next_node = head
            last_node = None
            while next_node:
                a, b, c = get_list(next_node, num)
                root = None
                last = None
                while a and b:
                    if not root:
                        if a.val <= b.val:
                            root = a
                            a = a.next
                        else:
                            root = b
                            b = b.next
                        last = root
                        if last_node:
                            last_node.next = root
                        continue
                    if a.val <= b.val:
                        last.next = a
                        a = a.next
                    else:
                        last.next = b
                        b = b.next
                    last = last.next
                if a:
                    if last_node and not root:
                        last_node.next = a
                    if last:
                        last.next = a
                    else:
                        last = a
                    while a.next:
                        a = a.next
                    last_node = a
                if b:
                    if last_node and not root:
                        last_node.next = b
                    if last:
                        last.next = b
                    else:
                        last = b
                    while b.next:
                        b = b.next
                    last_node = b
                next_node = c
                if is_head:
                    head = root
                    is_head = False
            num *= 2
        return head


if __name__ == '__main__':
    so = Solution()
    root = ListNode(-1)
    root.next = ListNode(5)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(4)
    root.next.next.next.next = ListNode(0)
    re = so.sortList(root)
    print(re)
