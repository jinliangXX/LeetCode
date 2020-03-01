# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.result = 0

        def get_result(node: TreeNode, last):
            now = last * 10 + node.val
            if not node.left and not node.right:
                self.result += now
            else:
                if node.left:
                    get_result(node.left, now)
                if node.right:
                    get_result(node.right, now)

        get_result(root, 0)
        return self.result


if __name__ == '__main__':
    so = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(so.sumNumbers(root))
