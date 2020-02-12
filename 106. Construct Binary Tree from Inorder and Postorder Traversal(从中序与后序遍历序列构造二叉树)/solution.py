# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        now = TreeNode(postorder[-1])
        index_one = inorder.index(postorder[-1])
        if index_one < 1:
            now.right = self.buildTree(inorder[index_one + 1:],
                                       postorder[:-1])
            return now
        else:
            index_two = postorder.index(inorder[index_one - 1])
            now.left = self.buildTree(inorder[:index_one], postorder[:index_one])
            now.right = self.buildTree(inorder[index_one + 1:],
                                       postorder[index_one:-1])
        return now


if __name__ == '__main__':
    so = Solution()
    inorder = [2, 3, 1]
    postorder = [3, 2, 1]
    print(so.buildTree(inorder, postorder))
