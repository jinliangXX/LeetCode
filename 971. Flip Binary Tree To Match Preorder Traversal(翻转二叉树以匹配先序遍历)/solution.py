# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.result = list()
        self.index = -1
        if not root:
            return self.result

        def get_result(node: TreeNode):
            if not node or self.result == [-1]:
                return
            self.index += 1
            if node.val != voyage[self.index]:
                self.result = [-1]
            elif self.index + 1 < len(voyage) and node.left and node.left.val != voyage[
                self.index + 1]:
                self.result.append(node.val)
                get_result(node.right)
                get_result(node.left)
            else:
                get_result(node.left)
                get_result(node.right)

        get_result(root)
        return self.result


if __name__ == '__main__':
    so = Solution()
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    print(so.flipMatchVoyage(root, [1, 3, 2]))
