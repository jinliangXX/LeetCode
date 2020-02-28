# Definition for a Node.

'''
第二种方法与当前思路一样，只不过一层一层执行
遍历当前层节点，记录下一层左侧节点，不断完善下一层的next节点
'''

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None,
                 next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:

    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        def get_result(node: Node):
            if not node:
                return
            if node.left:
                if node.right:
                    node.left.next = node.right
                else:
                    now_next = node.next
                    while now_next:
                        if now_next.left:
                            node.left.next = now_next.left
                            break
                        elif now_next.right:
                            node.left.next = now_next.right
                            break
                        now_next = now_next.next
            if node.right:
                now_next = node.next
                while now_next:
                    if now_next.left:
                        node.right.next = now_next.left
                        break
                    elif now_next.right:
                        node.right.next = now_next.right
                        break
                    now_next = now_next.next
            self.connect(node.right)
            self.connect(node.left)

        get_result(root)
        return root


if __name__ == '__main__':
    so = Solution()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(7)
    so.connect(root)
