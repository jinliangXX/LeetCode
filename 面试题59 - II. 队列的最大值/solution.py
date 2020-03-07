import collections
'''
一个正常队列
一个双端队列，每次插入时，删除前面比它小的数
'''

class MaxQueue:

    def __init__(self):
        self.deque = collections.deque()
        self.max_deque = collections.deque()

    def max_value(self) -> int:
        if not self.max_deque:
            return -1
        return self.max_deque[0]

    def push_back(self, value: int) -> None:
        self.deque.append(value)
        while self.max_deque and self.max_deque[-1] < value:
            self.max_deque.pop()
        self.max_deque.append(value)

    def pop_front(self) -> int:
        if not self.deque:
            return -1
        result = self.deque.popleft()
        if result == self.max_deque[0]:
            self.max_deque.popleft()
        return result


if __name__ == '__main__':
    obj = MaxQueue()
    param_1 = obj.max_value()
    obj.push_back(1)
    obj.push_back(2)
    print(obj.max_value())
    param_3 = obj.pop_front()
    print(obj.max_value())
