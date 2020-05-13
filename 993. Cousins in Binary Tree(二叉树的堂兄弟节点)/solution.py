# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False
        self.x_node = None
        self.y_node = None

        def get_result(node: TreeNode, p=None, deep=0):
            if not node:
                return
            if node.val == x:
                self.x_node = (deep, p)
            elif node.val == y:
                self.y_node = (deep, p)
            get_result(node.left, node, deep + 1)
            get_result(node.right, node, deep + 1)

        get_result(root)
        return self.x_node[0] == self.y_node[0] and self.x_node[1] != self.y_node[1]
