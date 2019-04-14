# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        list_re = list()
        list_he = list()
        now = Node(head.val, head.next, None)
        list_re.append(now)
        list_he.append(head)
        now = now.next
        while now is not None:
            now_node = Node(now.val, now.next, None)
            list_re.append(now_node)
            list_he.append(now)
            now = now.next
        for i, node in enumerate(list_he):
            if i == len(list_he) - 1:
                if list_he[i].random is None:
                    list_re[i].random = None
                else:
                    index = list_he.index(
                        list_he[i].random)
                    list_re[i].random = list_re[index]
            if i == 0:
                continue
            list_re[i - 1].next = list_re[i]
            if list_he[i - 1].random is None:
                list_re[i - 1].random = None
            else:
                index = list_he.index(list_he[i - 1].random)
                list_re[i - 1].random = list_re[index]
        return list_re[0]



