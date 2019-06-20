# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge_two(l1: ListNode, l2: ListNode):
            root = ListNode(-1)
            now = root
            while l1 and l2:
                if l1.val <= l2.val:
                    now.next = l1
                    l1 = l1.next
                else:
                    now.next = l2
                    l2 = l2.next
                now = now.next
            if not l1:
                now.next = l2
            if not l2:
                now.next = l1
            return root.next

        # 分治思想
        if not lists:
            return None
        lenght = len(lists)
        while lenght > 1:
            num = 0
            for i in range(0, lenght, 2):
                if i + 1 == lenght:
                    lists[num] = lists[i]
                    continue
                lists[num] = merge_two(lists[i], lists[i + 1])
                num += 1
            lenght -= num
        return lists[0]

if __name__ == '__main__':
    s = None
    if s:
        print('a')
