# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if val > root.val:
            node = TreeNode(val)
            node.left = root
            return node

        def get_result(node: TreeNode, parent: TreeNode):
            if not node:
                parent.right = TreeNode(val)
                return
            if val > node.val:
                now = TreeNode(val)
                now.left = node
                parent.right = now
            else:
                get_result(node.right, node)

        get_result(root, None)
        return root
