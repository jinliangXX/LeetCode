# Definition for a binary tree node.
from queue import Queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue_left, queue_right = Queue(), Queue()
        queue_left.put(root)
        while not queue_left.empty():
            lenght = queue_left.qsize()
            if lenght == 1 and queue_right.empty():
                node = queue_left.get()
                if node:
                    queue_left.put(node.left)
                    queue_right.put(node.right)
            else:
                for _ in range(lenght):
                    node_left = queue_left.get()
                    node_right = queue_right.get()
                    if node_left and node_right:
                        if node_left.val != node_right.val:
                            return False
                        queue_left.put(node_left.right)
                        queue_left.put(node_left.left)
                        queue_right.put(node_right.left)
                        queue_right.put(node_right.right)
                    else:
                        if node_left != node_right:
                            return False
        return True

'''
叶子节点数 n/2
空间复杂度O(n/2)=O(n)
'''