# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        def con(root: Node):
            if not root.left:
                return
            root.left.next = root.right
            if root.next and root.next.left:
                root.right.next = root.next.left
            con(root.left)
            con(root.right)

        if not root:
            return root
        con(root)
        return root
