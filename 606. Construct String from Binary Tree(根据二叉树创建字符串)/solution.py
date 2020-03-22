# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ''
        result = str(t.val)
        left_result = ''
        if t.left:
            left_result = self.tree2str(t.left)
        if t.right:
            right_result = self.tree2str(t.right)
            result += '(' + left_result + ')' + '(' + right_result + ')'
        else:
            result += '(' + left_result + ')' if left_result else ''
        return result
