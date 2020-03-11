# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """

        def xianxu(root: TreeNode):
            if not root:
                return []
            now = [root.val]
            return now + xianxu(root.left) + xianxu(root.right)

        return ' '.join(str(i) for i in xianxu(root))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        xianxu = list(map(int, data.split()))
        zhongxu = sorted(xianxu)

        def get_result(xianxu: List, zhongxu: List):
            if not xianxu:
                return None
            root = TreeNode(xianxu[0])
            index_now = zhongxu.index(xianxu[0])
            if index_now > 0:
                root.left = get_result(xianxu[1:index_now + 1], zhongxu[:index_now])
            if index_now < len(zhongxu) - 1:
                root.right = get_result(xianxu[index_now + 1:], zhongxu[index_now + 1:])
            return root

        return get_result(xianxu, zhongxu)

    # Your Codec object will be instantiated and called as such:
    # codec = Codec()
    # codec.deserialize(codec.serialize(root))


if __name__ == '__main__':
    so = Codec()
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    so.deserialize(so.serialize(root))
