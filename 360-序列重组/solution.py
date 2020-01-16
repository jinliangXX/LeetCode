import sys


class Solution:

    def get_nums(self, nums1, nums2, n, m):
        result, index1 = list(), set()
        for num in range(m - 1, 0, -1):
            for i, now1 in enumerate(nums1):
                for j, now2 in enumerate(nums2):
                    if len(result) == n:
                        return result
                    if (now1 + now2) % m == num:
                        result.append((now1 + now2) % m)
                        index1.add(i)
                        nums2.pop(j)
                        break
            for index in index1:
                nums1.pop(index)
            index1.clear()
        return result


if __name__ == '__main__':
    [n, m] = list(map(int, sys.stdin.readline().strip().split()))
    nums1 = list(map(int, sys.stdin.readline().strip().split()))
    nums2 = list(map(int, sys.stdin.readline().strip().split()))
    so = Solution()
    result = so.get_nums(nums1, nums2, n, m)
    print(' '.join(str(i) for i in result))
