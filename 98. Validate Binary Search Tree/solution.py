# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root):
        if root is None:
            return True
        return self.pre_order(root, None, None)

    def pre_order(self, root, min_num, max_num):
        '''
        前序
        :param root:
        :return:
        '''
        if min_num is not None and root.val <= min_num:
            return False
        if max_num is not None and root.val >= max_num:
            return False
        if root.left is not None:
            if not self.pre_order(
                    root.left, min_num,
                    self.min(max_num, root.val)):
                return False
        if root.right is not None:
            if not self.pre_order(
                    root.right, self.max(min_num, root.val),
                    max_num):
                return False
        return True

    def min(self, a, b):
        if a is None:
            return b
        if b is None:
            return a
        return min(a, b)

    def max(self, a, b):
        if a is None:
            return b
        if b is None:
            return a
        return max(a, b)


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(solution.isValidBST(root))
