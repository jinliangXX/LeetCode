# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        def get_result(node: TreeNode):
            if not node:
                return (-1, None)
            left_result = get_result(node.left)
            right_result = get_result(node.right)
            if left_result[0] == right_result[0]:
                return (left_result[0] + 1, node)
            elif left_result[0] > right_result[0]:
                return (left_result[0] + 1, left_result[1])
            else:
                return (right_result[0] + 1, right_result[1])

        return get_result(root)[1]
