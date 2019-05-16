# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        result = list()
        stack = list()
        while True:
            if root is None and len(stack) < 1:
                break
            if root is None:
                now = stack.pop()
                result.append(now.val)
                root = now.right
                continue
            if root.left is not None:
                stack.append(root)
                root = root.left
                continue
            result.append(root.val)
            if root.right is not None:
                root = root.right
                continue
            root = None
        return result

    def inorder_tree(self, root, result):
        '''
        中序遍历
        :param root:
        :return:
        '''
        if root is None:
            return
        self.inorder_tree(root.left, result)
        result.append(root.val)
        self.inorder_tree(root.right, result)


if __name__ == '__main__':
    solution = Solution()
