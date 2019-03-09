# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import List


class Solution:
    def buildTree(self, preorder: List[int],
                  inorder: List[int]) -> TreeNode:




