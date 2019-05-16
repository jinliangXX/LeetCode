"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""


class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


class NestedInteger(object):
    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        if isinstance(object, int):
            return True
        return False

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        if self.isInteger():
            return object
        return None

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        if not self.isInteger():
            return object
        return None


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.result = list()
        for one in nestedList:
            self.get_cal(one)
        self.i = 0

    def get_cal(self, nestedList):
        if nestedList.isInteger():
            self.result.append(nestedList.getInteger())
        else:
            for i, num in enumerate(nestedList.getList()):
                self.get_cal(num)

    def next(self):
        """
        :rtype: int
        """
        num = self.result[self.i]
        self.i += 1
        return num

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.i < len(self.result):
            return True
        return False


# Your NestedIterator object will be instantiated and called as such:
nestedList = [NestedInteger(1), NestedInteger([4, [6]])]
i, v = NestedIterator(nestedList), []
while i.hasNext(): v.append(i.next())
