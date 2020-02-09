# Definition for a binary tree node.
from queue import Queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def shunxu_array(node: TreeNode):
            result = list()
            queue = Queue()
            if not node:
                return result
            queue.put(node)
            while not queue.empty():
                now = queue.get()
                if now:
                    result.append(now.val)
                    queue.put(now.left)
                    queue.put(now.right)
                else:
                    result.append(None)
            return result

        result_p = shunxu_array(p)
        result_q = shunxu_array(q)
        return result_p == result_q
