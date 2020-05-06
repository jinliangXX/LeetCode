# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        deque = collections.deque()
        deque.append(root)
        is_all = False
        while len(deque) > 0:
            size = len(deque)
            for _ in range(size):
                node = deque.popleft()
                if node.left:
                    if is_all: return False
                    deque.append(node.left)
                else:
                    is_all = True
                if node.right:
                    if is_all: return False
                    deque.append(node.right)
                else:
                    is_all = True
        return True
