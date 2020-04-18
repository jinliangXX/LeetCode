# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        head = root
        while root:
            if val < root.val:
                if root.left:
                    root = root.left
                else:
                    root.left = TreeNode(val)
                    break
            else:
                if root.right:
                    root = root.right
                else:
                    root.right = TreeNode(val)
                    break
        return head
