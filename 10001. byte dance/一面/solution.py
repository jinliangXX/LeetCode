import random

from queue import Queue

from typing import List


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def get_list_6(self, peoples: dict) -> List[int]:
        length, start, result = sum(peoples.values()), 0, list()
        tickets = [i for i in range(length)]
        for people in peoples:
            peoples[people] = tickets[start:start + peoples[people]]
            start += peoples[people]
        start = 0
        for _ in range(100):
            index = random.randint(start, len(tickets))
            for people in peoples:
                if tickets[index] in peoples[people]:
                    result.append(people)
                    for num in peoples[people]:
                        tickets[start], tickets[num] = tickets[num], tickets[start]
                    break
        return result

    def get_list_5(self, peoples: dict) -> List[int]:
        length, start, result = sum(peoples.values()), 0, list()
        tickets = [0 for _ in range(length - 100)]
        tickets.extend([1 for _ in range(100)])
        for people in peoples:
            for _ in range(peoples[people]):
                index = random.randint(start, length)
                tickets[start], tickets[index] = tickets[index], tickets[start]
                if tickets[start] == 1:
                    result.append(people)
                    start += 1
                    break
                start += 1
        return result

    def get_list4(self, nums: List[int]) -> List[List[int]]:
        result = list()
        for num in range(2 ** len(nums)):
            nows = list()
            index = 0
            while num >= 1:
                if num & 1 == 1:
                    nows.append(nums[index])
                index += 1
                num >>= 1
            result.append(nows)
        return result

    def get_list3(self, nums: List[int]) -> List[List[int]]:
        result = list()
        for num in range(2 ** len(nums)):
            nows = list()
            s = bin(num)
            for i, char in enumerate(s):
                if char == '1':
                    nows.append(nums[i])
            result.append(nows)
        return result

    def get_list_2(self, root: Node) -> List[List[int]]:
        if not root.left and not root.right:
            return [[root.val]]
        else:
            now_list = [[]]
            if root.left:
                now_list.extend(self.get_list_2(root.left))
            if root.right:
                now_list.extend((self.get_list_2(root.right)))
            for nums in now_list:
                nums.insert(0, root.val)
            return now_list

    def get_list(self, root: Node) -> List[List[int]]:
        result = list()
        if not root:
            return result
        que = Queue()
        que.put(root)
        while que:
            length = que.qsize()
            now_list = list()
            for _ in range(length):
                node = que.get()
                now_list.append(node.val)
                if node.left:
                    que.put(node.left)
                if node.right:
                    que.put(node.right)
            result.append(now_list)
        return result
