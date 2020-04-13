# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        self.result = list()

        def get_result(node: Node, deep=0):
            if not node:
                return
            if deep < len(self.result):
                self.result[deep].append(node.val)
            else:
                self.result.append([node.val])
            for child in node.children:
                get_result(child, deep + 1)

        get_result(root)
        return self.result
