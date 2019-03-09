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
        stack = list()
        if root is None:
            return result
        while True:
            if root.left is not None or root.right is not None:
                stack.append(TreeNode(root.val))
            else:
                result.append(root.val)
                if len(stack) > 0:
                    root = stack.pop()
                else:
                    break
                continue
            if root.left is not None:
                if root.right is not None:
                    stack.append(root.right)
                root = root.left
            else:
                root = root.right
        return result



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
