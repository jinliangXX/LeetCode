# Definition for a binary tree node.
import collections
import math


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class CBTInserter:

    def __init__(self, root: TreeNode):
        self.tree = list()
        queue = collections.deque()
        queue.append(root)
        while len(queue) > 0:
            node = queue.popleft()
            self.tree.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def insert(self, v: int) -> int:
        node = TreeNode(v)
        index = math.ceil(len(self.tree) / 2) - 1
        self.tree.append(node)
        if (len(self.tree) - 1) % 2 == 0:
            self.tree[index].right = node
        else:
            self.tree[index].left = node
        return self.tree[index].val

    def get_root(self) -> TreeNode:
        return self.tree[0]

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
