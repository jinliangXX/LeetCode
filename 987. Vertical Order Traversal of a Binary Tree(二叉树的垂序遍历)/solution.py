# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        self.result = dict()

        def get_result(node: TreeNode, x=0, y=0):
            if not node:
                return
            if x in self.result:
                self.result[x].append((y, node.val))
            else:
                self.result[x] = [(y, node.val)]
            get_result(node.left, x - 1, y + 1)
            get_result(node.right, x + 1, y + 1)

        get_result(root)
        output = list()
        for now in sorted(self.result):
            output.append([i[1] for i in sorted(self.result[now])])
        return output


if __name__ == '__main__':
    so = Solution()
    input = TreeNode(0)
    input.left = TreeNode(1)
    input.right = TreeNode(2)
    print(so.verticalTraversal(input))
