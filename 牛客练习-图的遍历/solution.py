import sys


class Solution:

    def get_num(self, nums: dict, n: int) -> int:
        stack, views, now, result = list(), set([1]), 1, 0
        while len(views) < n:
            if now in nums:
                index = None
                for num in nums[now]:
                    if num not in views:
                        index = num
                        break
                if index:
                    stack.append(now)
                    nums[now].remove(index)
                    now = index
                else:
                    nums.pop(now)
                    if len(stack) + 1 > result:
                        result = len(stack) + 1
                    now = stack.pop()
            views.add(now)
        if len(stack) + 1 > result:
            result = len(stack) + 1
        return (n - result) * 2 + result - 1


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip('\n'))
    nums = dict()
    for _ in range(n - 1):
        [x, y] = list(map(int, sys.stdin.readline().strip().split()))
        if x in nums:
            nums[x].append(y)
        else:
            nums[x] = ([y])
        if y in nums:
            nums[y].append(x)
        else:
            nums[y] = ([x])
    so = Solution()
    print(so.get_num(nums, n))
