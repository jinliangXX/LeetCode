# Definition for a binary tree node.


'''
迭代中序遍历

仔细分析一下，该循环只有在节点有右子树的时候才需要进行，也就是不是每一次操作都需要循环的，循环的次数加上初始化的循环总共会有O(n)次操作，均摊到每一次next()的话平均时间复杂度则是O(n)/n=O(1)，因此可以确定该实现方式满足O(1)的要求。

这种分析方式称为摊还分析，详细的学习可以看看**《算法导论》- 第17章 摊还分析**

'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = list()
        self.node = root
        while root and self.node.left:
            self.stack.append(self.node)
            self.node = self.node.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        result = self.node.val
        if self.node.right:
            self.node = self.node.right
            while self.node.left:
                self.stack.append(self.node)
                self.node = self.node.left
        else:
            if not self.stack:
                self.node = None
            else:
                self.node = self.stack.pop()
        return result

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.node != None


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
if __name__ == '__main__':
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    so = BSTIterator(root)
    print(so.next())
    print(so.next())
    print(so.next())
    print(so.hasNext())
