import collections

'''
使用两个队列实现栈
一个队列不断加入新数据，另一个队列仅保存栈顶元素
当涉及到pop操作，需要循环将第一个队列的数据移到第二个队列中，以获取栈顶元素
python实现时，最好不要使用Queue类，使用collections.deque比较好



方法三 （一个队列， 压入 - O(n)O(n)， 弹出 - O(1)O(1)）
上面介绍的两个方法都有一个缺点，它们都用到了两个队列。下面介绍的方法只需要使用一个队列。

算法

压入（push）

当我们将一个元素从队列入队的时候，根据队列的性质这个元素会存在队列的后端。

但当我们实现一个栈的时候，最后入队的元素应该在前端，而不是在后端。为了实现这个目的，每当入队一个新元素的时候，我们可以把队列的顺序反转过来。

'''
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.deque = [collections.deque(), collections.deque()]
        self.top_deque = 1

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if len(self.deque[self.top_deque]) > 0:
            self.deque[1 - self.top_deque].append(self.deque[self.top_deque].pop())
        self.deque[self.top_deque].append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.empty():
            return None
        top = self.deque[self.top_deque].pop()
        while len(self.deque[1 - self.top_deque]) > 1:
            self.deque[self.top_deque].append(self.deque[1 - self.top_deque].popleft())
        self.top_deque = 1 - self.top_deque
        return top

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.deque[self.top_deque][0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.deque[1 - self.top_deque]) == 0 and len(
            self.deque[self.top_deque]) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
