# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        def addRow(node: TreeNode, deep=1):
            if not node:
                return
            if deep == d - 1:
                node_left, node_right = TreeNode(v), TreeNode(v)
                node_left.left = node.left
                node_right.right = node.right
                node.left, node.right = node_left, node_right
            addRow(node.left, deep + 1)
            addRow(node.right, deep + 1)

        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        else:
            addRow(root)
            return root
