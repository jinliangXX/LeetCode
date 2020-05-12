# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        if not root:
            return ""

        self.result = None

        def get_result(node: TreeNode, last=''):
            if not node:
                return
            now = chr(node.val + ord('a'))
            if not node.left and not node.right:
                if self.result is None:
                    self.result = now + last
                else:
                    self.result = min(self.result, now + last)
            get_result(node.left, now + last)
            get_result(node.right, now + last)

        get_result(root)
        return self.result


if __name__ == '__main__':
    a = 'b'
    b = 'ba'
    print(min(a, b))

    so = Solution()
    input = TreeNode(4)
    input.left = TreeNode(0)
    input.right = TreeNode(1)
    input.left.left = TreeNode(1)
    print(so.smallestFromLeaf(input))
