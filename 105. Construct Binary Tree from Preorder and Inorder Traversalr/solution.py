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
        self.root = None
        if len(preorder) == 0:
            return self.root
        self.init_tree(preorder, inorder, None)
        return self.root

    def init_tree(self, preorder, inorder, root):
        if root is None:
            root = TreeNode(preorder[0])
            self.root = root
        index = inorder.index(root.val)
        if index == 0:
            pass
        elif index == 1:
            left = TreeNode(inorder[0])
            root.left = left
        else:
            left = TreeNode(preorder[1])
            root.left = left
            self.init_tree(preorder[1:index],
                           inorder[0:index], root.left)
        if len(inorder) - index == 1:
            pass
        elif len(inorder) - index == 2:
            right = TreeNode(inorder[index + 1])
            root.right = right
        else:
            right = TreeNode(preorder[index + 1])
            root.right = right
            self.init_tree(preorder[index + 1:],
                           inorder[index + 1:], root.right)


if __name__ == '__main__':
    so = Solution()
    a = so.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print(a)
