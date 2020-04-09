# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        result = list()

        def get_result(node: TreeNode, deep=0):
            if not node:
                if deep < len(result):
                    result[deep][1] += 1
                if deep + 1 < len(result):
                    get_result(None, deep + 1)
                    get_result(None, deep + 1)
                return
            if deep < len(result):
                result[deep] = [result[deep][0] + result[deep][1] + 1, 0]
            else:
                result.append([1, 0])
            get_result(node.left, deep + 1)
            get_result(node.right, deep + 1)

        get_result(root)
        return max(result, key=lambda x: x[0])[0]
