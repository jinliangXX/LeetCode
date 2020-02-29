# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def maxPathSum(self, root: TreeNode) -> int:
        self.result = int(-100)

        def get_result(node: TreeNode) -> int:
            if not node:
                return int(-100)
            left_sum = get_result(node.left)
            right_sum = get_result(node.right)
            node_result = max(node.val, left_sum + node.val, right_sum + node.val)
            not_node_result = max(left_sum, right_sum, left_sum + node.val + right_sum)
            if not_node_result >= node_result:
                self.result = max(self.result, not_node_result)
            return node_result

        now = get_result(root)
        self.result = max(self.result, now)
        return self.result


if __name__ == '__main__':
    so = Solution()
    root = TreeNode(1)
    root.left = TreeNode(-2)
    root.right = TreeNode(-3)
    root.right.left = TreeNode(-2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.left.left.left = TreeNode(-1)
    print(so.maxPathSum(root))
