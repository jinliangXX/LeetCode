# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int, last=False) -> int:
        if not root:
            return 0
        result = 0
        if not last:
            result += self.pathSum(root.left, sum)
            result += self.pathSum(root.right, sum)
        now = sum - root.val
        if now == 0:
            result += 1
        result += self.pathSum(root.left, now, True)
        result += self.pathSum(root.right, now, True)
        return result
