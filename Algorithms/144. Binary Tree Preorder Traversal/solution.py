# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = list()
        if root is None:
            return result
        self.pre_order(root, result)
        return result

    def pre_order(self, root, result):
        '''
        先序
        :param root:
        :return:
        '''
        if root is None:
            return
        result.append(root.val)
        self.pre_order(root.left, result)
        self.pre_order(root.right, result)
