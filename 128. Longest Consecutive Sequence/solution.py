from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        map_dict = dict()
        for num in nums:
            if num not in map_dict:
                left = map_dict.get(num - 1, 0)
                right = map_dict.get(num + 1, 0)
                now = left + 1 + right

                if now > result:
                    result = now

                map_dict[num] = now  # 必须要有，去重
                map_dict[num - left] = now
                map_dict[num + right] = now
        return result

# from typing import List
#
#
# class Node:
#     def __init__(self, val=0, next=None, previous=None):
#         self.val = val
#         self.next = next
#         self.previous = previous
#
#
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         map_num = dict()
#         root = Node()
#         now = root
#         for num in nums:
#             node = Node(num, None, now)
#             map_num[num] = node
#             now.next = node
#             now = node
#         result = 0
#         root = root.next
#         while root is not None:
#             num = root.val
#             now_result = 1
#             left = num - 1
#             right = num + 1
#             while left in map_num:
#                 now_result += 1
#                 node = map_num[left]
#                 # 在链表中删除节点
#                 a = node.previous
#                 b = node.next
#                 a.next = b
#                 if b is not None:
#                     b.previous = a
#                 left -= 1
#             while right in map_num:
#                 now_result += 1
#
#                 node = map_num[right]
#                 # 在链表中删除节点
#                 a = node.previous
#                 b = node.next
#                 a.next = b
#                 if b is not None:
#                     b.previous = a
#                 right += 1
#             if now_result > result:
#                 result = now_result
#             root = root.next
#         return result
