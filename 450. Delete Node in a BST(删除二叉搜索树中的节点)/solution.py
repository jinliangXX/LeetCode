# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def deleteNode(self, root: TreeNode, key: int, last_node=None) -> TreeNode:
        if not root:
            return root
        if root.val == key:
            if root.left:
                last, node = root, root.left
                while node.right:
                    last = node
                    node = node.right
                root.val = node.val
                if root == last:
                    root.left = node.left
                else:
                    last.right = node.left
            elif root.right:
                last, node = root, root.right
                while node.left:
                    last = node
                    node = node.left
                root.val = node.val
                if root == last:
                    root.right = node.right
                else:
                    last.left = node.right
            else:
                root = None
        elif key < root.val:
            root.left = self.deleteNode(root.left, key, root)
        else:
            root.right = self.deleteNode(root.right, key, root)
        return root
