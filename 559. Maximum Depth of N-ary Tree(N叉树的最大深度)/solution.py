# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.result = 0
        if not root:
            return self.result

        def get_result(node: 'Node', deep=1):
            if not node:
                return
            self.result = max(deep, self.result)
            if node.children:
                for child in node.children:
                    get_result(child, deep + 1)

        get_result(root)
        return self.result
