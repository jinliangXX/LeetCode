import sys


class Solution(object):
    def minmaxGasDist(self, nums, n, m):
        result = [nums[i + 1] - nums[i] for i in range(m - 1)]
        now = min(result)
        for i in range(m, n):
            if min(result) < nums[i] - nums[i - 1]:
                index = result.index((min(result)))
                if (index >= 1 and index < len(result) - 1 and result[index - 1] < result[
                    index + 1]) or (index == len(result) - 1 and result[index - 1] < m):
                    index = index - 1
            else:
                index = len(result) - 1
            for j, re in enumerate(result):
                if j >= index:
                    if j < len(result) - 1:
                        result[j] = re + result[j + 1]
                    else:
                        result[j] += i
        return min(result)


if __name__ == '__main__':
    [n, m] = list(map(int, sys.stdin.readline().strip().split()))
    nums = list(map(int, sys.stdin.readline().strip().split()))
    so = Solution()
    print(so.minmaxGasDist(nums, n, m))
