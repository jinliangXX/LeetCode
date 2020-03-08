# Definition for a binary tree node.
from typing import List
'''
https://leetcode-cn.com/problems/house-robber-iii/solution/san-chong-fang-fa-jie-jue-shu-xing-dong-tai-gui-hu/
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        def get_result(node: TreeNode) -> List:
            if not node:
                return [0, 0]
            left_result = get_result(node.left)
            right_result = get_result(node.right)
            return [node.val + left_result[1] + right_result[1],
                    max(left_result) + max(right_result)]

        return max(get_result(root))


if __name__ == '__main__':
    so = Solution()
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right = TreeNode(3)
    root.right.right = TreeNode(1)
    print(so.rob(root))
