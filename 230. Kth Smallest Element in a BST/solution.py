# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = list()
        num = 0
        while root is not None:
            if root.left is not None:
                stack.append(root)
                root = root.left
            elif root.right is not None:
                num += 1
                if num == k:
                    return root.val
                root = root.right
            else:
                num += 1
                if num == k:
                    return root.val
                if len(stack) < 1:
                    break
                root = stack.pop()
                root.left = None


'''
O(N)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.result = list()
        self.mid_num(root)
        return self.result[k - 1]

    def mid_num(self, root: TreeNode):
        if root is None:
            return
        self.mid_num(root.left)
        self.result.append(root.val)
        self.mid_num(root.right)
'''
