# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[
        List[int]]:
        self.result = list()
        result = self.get_cal(root, 0)
        for i, list_now in enumerate(self.result):
            if i % 2 == 1:
                list_now = list_now[::-1]
        return self.result

    def get_cal(self, root, index):
        if root is None:
            return
        if len(self.result) <= index:
            new_list = list()
            self.result.append(new_list)
        self.result[index].append(root.val)
        now = index + 1
        self.get_cal(root.left, now)
        self.get_cal(root.right, now)


if __name__ == '__main__':
    a = [2, 3, 4, 5, 6, 7, 8, 9]
    for now in a:
        now = now + 1
    print(a)
