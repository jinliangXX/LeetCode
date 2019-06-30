# Definition for a binary tree node.
import json

from queue import Queue


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = list()
        if not root:
            return str(result)
        queue = Queue()
        queue.put(root)
        while not queue.empty():
            lenght = queue.qsize()
            is_null = False
            for _ in range(lenght):
                now = queue.get()
                result.append(now.val) if now else result.append(now)
                if now:
                    if now.left or now.right:
                        is_null = True
                    queue.put(now.left)
                    queue.put(now.right)
            if not is_null:
                break
        return json.dumps(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        result = json.loads(data)
        if not result:
            return None
        queue = Queue()
        root = None
        index = 0
        while index < len(result):
            if queue.empty():
                root = TreeNode(result[index])
                queue.put(root)
                index += 1
                continue
            lenght = queue.qsize()
            for _ in range(lenght):
                node = queue.get()
                if not node:
                    continue
                if index + 1 >= len(result):
                    return root
                node.left = TreeNode(result[index]) if result[index] is not None else None
                node.right = TreeNode(result[index + 1]) if result[
                                                                index + 1] is not None else None
                index += 2
                queue.put(node.left)
                queue.put(node.right)
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    codec = Codec()
    a = codec.deserialize(codec.serialize(root))
    print(a)
