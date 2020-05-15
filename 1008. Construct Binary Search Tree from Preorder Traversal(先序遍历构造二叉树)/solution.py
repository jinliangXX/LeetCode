# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        inorder = sorted(preorder)

        def get_result(pre_num: List, in_num: List):
            if not pre_num:
                return
            node = TreeNode(pre_num[0])
            index = in_num.index(pre_num[0])
            if in_num.index(pre_num[0]) > 0:
                node.left = get_result(pre_num[1:index + 1],
                                       in_num[0:index])
            if in_num.index(pre_num[0]) + 1 < len(pre_num):
                node.right = get_result(pre_num[index + 1:],
                                        in_num[index + 1:])
            return node

        root = get_result(preorder, inorder)
        return root


if __name__ == '__main__':
    so = Solution()
    print(so.bstFromPreorder([8, 5, 1, 7, 10, 12]))
