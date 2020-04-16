# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        result, stack = list(), [root]
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
            if node.children:
                stack.extend(node.children)
        return result[::-1]
