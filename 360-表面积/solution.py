# utf-8
import sys


class Solution:

    def get_num(self, nums, n, m):
        result = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                now = 4 * nums[i][j] + 2 - 2 * min(nums[i - 1][j], nums[i][j]) - 2 * min(
                    nums[i][j - 1], nums[i][j])
                result += now
        return result


if __name__ == '__main__':
    [n, m] = list(map(int, sys.stdin.readline().strip().split()))
    nums = [[0 for _ in range(m + 1)]]
    for _ in range(n):
        input = [0]
        input.extend(list(map(int, sys.stdin.readline().strip().split())))
        nums.append(input)
    so = Solution()
    print(str(so.get_num(nums, n, m)))
