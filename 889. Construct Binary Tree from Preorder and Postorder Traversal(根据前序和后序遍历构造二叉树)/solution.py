# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre or not post:
            return None
        root_val = pre[0]
        node = TreeNode(root_val)
        # for i in range(1,len(pre)):
        #     if post.index(pre[1])
        if len(pre) > 1:
            length = post.index(pre[1]) + 1
            node.left = self.constructFromPrePost(pre[1:1 + length], post[:length])
            node.right = self.constructFromPrePost(pre[1 + length:], post[length:-1])
        return node
