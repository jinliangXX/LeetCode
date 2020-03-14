# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return list()
        self.result = dict()
        self.max_number = 0

        def get_sum(node: TreeNode):
            if not node:
                return 0
            left_sum = get_sum(node.left)
            right_sum = get_sum(node.right)
            if node.left:
                self.result[left_sum] = self.result.get(left_sum, 0) + 1
                self.max_number = max(self.max_number, self.result[left_sum])
            if node.right:
                self.result[right_sum] = self.result.get(right_sum, 0) + 1
                self.max_number = max(self.max_number, self.result[right_sum])
            return node.val + left_sum + right_sum

        root_sum = get_sum(root)
        self.result[root_sum] = self.result.get(root_sum, 0) + 1
        self.max_number = max(self.max_number, self.result[root_sum])
        return [index for index in self.result if self.result[index] == self.max_number]


if __name__ == '__main__':
    so = Solution()
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(-3)
    print(so.findFrequentTreeSum(root))
