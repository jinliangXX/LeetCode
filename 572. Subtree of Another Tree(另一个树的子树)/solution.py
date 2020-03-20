# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def is_same(node1: TreeNode, node2: TreeNode):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return node1.val == node2.val and is_same(node1.left, node2.left) and is_same(
                node1.right, node2.right)

        def get_result(node: TreeNode):
            if not node:
                return False
            if is_same(node, t):
                return True
            if get_result(node.left):
                return True
            if get_result(node.right):
                return True
            return False

        return get_result(s)
