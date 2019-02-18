# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = list()


    def post_order(self, root, result):
        '''
        后序
        :param root:
        :param result:
        :return:
        '''
        if root is None:
            return
        self.post_order(root.left, result)
        self.post_order(root.right, result)
        result.append(root.val)
