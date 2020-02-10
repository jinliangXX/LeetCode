# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.left, self.right, self.last = None, None, None

        def midd(node: TreeNode):
            if not node:
                return
            midd(node.left)
            if self.left:
                if node.val < self.right.val:
                    self.right = node
                pass
            else:
                if self.last and node.val < self.last.val:
                    self.left = self.last
                    self.right = node
            self.last = node
            midd(node.right)

        midd(root)
        if self.left and self.right:
            self.left.val, self.right.val = self.right.val, self.left.val


if __name__ == '__main__':
    so = Solution()
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(2)
    so.recoverTree(root)
    pass
