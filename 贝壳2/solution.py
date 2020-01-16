import sys
from collections import Counter


class Solution:

    def get_num(self, n, nums):
        num_map = Counter(nums)
        num_set = set(nums)
        result, index, index_num = 0, None, num_set.
        while index or index_num < len(num_set):
            if index:
                i = index
            else:
                i = num_set.remove()
                index_num += 1
            if num_map[i] >= 2:
                index = i + 1
                if index == index_num:
                    index_num += 1
            else:
                index = None
            while num_map[i] >= 2:
                num_map[i] -= 2
                num_map[i + 1] = num_map.get(i + 1, 0) + 1
            if num_map[i] == 1:
                result += 1
            num_map.pop(i)
        return result


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip('\n'))
    nums = list(map(int, sys.stdin.readline().strip().split()))
    so = Solution()
    print(so.get_num(n, nums))
