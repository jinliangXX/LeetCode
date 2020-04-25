# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    result = {0: [], 1: [TreeNode(0)]}

    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N not in self.result:
            noe_result = list()
            for i in range(1, N, 2):
                j = N - 1 - i
                for left in self.allPossibleFBT(i):
                    for right in self.allPossibleFBT(j):
                        node = TreeNode(0)
                        node.left = left
                        node.right = right
                        noe_result.append(node)
            self.result[N] = noe_result

        return self.result[N]
