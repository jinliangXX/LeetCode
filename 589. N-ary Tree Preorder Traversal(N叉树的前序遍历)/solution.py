# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = list()
        stack = list()
        if not root:
            return result
        stack.append(root)
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.children:
                stack.extend(node.children[::-1])

        return result


if __name__ == '__main__':
    so = Solution()
    root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
    print(so.preorder(root))
