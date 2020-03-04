# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def get_deep(self, node: TreeNode):
        if not node:
            return 0
        deep = 1
        left_node, right_node = node, node
        while left_node.left and right_node.right:
            deep += 1
            left_node = left_node.left
            right_node = right_node.right
        return deep if not left_node and not right_node else -1

    def countNodes(self, root: TreeNode) -> int:
        deep = self.get_deep(root)
        if deep > 0:
            return 2 ** deep
        elif deep == 0:
            return 0
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
