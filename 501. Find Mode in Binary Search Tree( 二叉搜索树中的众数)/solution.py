# Definition for a binary tree node.
from typing import List

'''
边进行中序遍历，边找众数
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.result, self.num = list(), 0
        self.leng, self.number = 0, None

        def zhongxu(root: TreeNode):
            if not root:
                return None
            zhongxu(root.left)
            if root.val == self.number:
                self.leng += 1
            else:
                self.number = root.val
                self.leng = 1
            if self.leng > self.num:
                if len(self.result) != 1 or self.result[0] != root.val:
                    self.result.clear()
                    self.result.append(root.val)
                self.num = self.leng
            elif self.leng == self.num:
                self.result.append(root.val)
            zhongxu(root.right)

        zhongxu(root)
        return self.result
