class Node:
    def __init__(self, key: int, val: int, next, last):
        self.val = val
        self.key = key
        self.next = next
        self.last = last


class LRUCache:

    def __init__(self, capacity: int):
        self.result = dict()
        self.root = Node(capacity, capacity, None, None)
        self.end = self.root

    def get(self, key: int) -> int:
        if key in self.result:
            node = self.result[key]
            if self.root.next is not node:
                if node.next is not None:
                    next_node = node.next
                    next_node.last = node.last
                else:
                    self.end = node.last
                node_last = node.last
                node_last.next = node.next
                if self.root.next is not None:
                    next_node = self.root.next
                    next_node.last = node
                    node.next = next_node

                self.root.next = node
                node.last = self.root

            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.result:
            node = self.result[key]
            node.val = value
            if self.root.next is not node:
                if node.next is not None:
                    next_node = node.next
                    next_node.last = node.last
                else:
                    self.end = node.last
                node_last = node.last
                node_last.next = node.next
                if self.root.next is not None:
                    next_node = self.root.next
                    next_node.last = node
                    node.next = next_node

                self.root.next = node
                node.last = self.root
        else:
            node = Node(key, value, None, None)
            if self.root.next is not None:
                next_node = self.root.next
                next_node.last = node
                node.next = next_node
            else:
                self.end = node
            self.root.next = node
            node.last = self.root
            self.result[key] = node
            if len(self.result) > self.root.val:
                self.result.pop(self.end.key)
                end_last = self.end.last
                self.end = end_last
                end_last.next = None


# if __name__ == '__main__':
#     cache = LRUCache(1)
#     cache.put(2, 1)
#     # cache.put(2, 1)
#     print(cache.get(2))
#     cache.put(3, 2)
#     print(cache.get(2))
#     # cache.put(4, 4)
#     print(cache.get(3))
# print(cache.get(3))
# print(cache.get(4))
