# Definition for a binary tree node.
'''
此题与求最大值不同，这个题肯定会到叶子节点，即最终是两个叶子节点之间的距离

因此可以通过求深度的函数
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode, is_root=False) -> int:
        self.result = 0

        def deep(node: TreeNode):
            if not node:
                return 0
            left_deep = deep(node.left)
            right_deep = deep(node.right)
            self.result = max(self.result, left_deep + right_deep)
            return max(left_deep, right_deep) + 1

        deep(root)
        return self.result
