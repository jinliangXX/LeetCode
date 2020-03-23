from typing import List


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        result = 0
        chongfu = 0
        A.append(80000)
        for i in range(1, len(A)):
            if A[i] == A[i - 1]:
                result -= A[i]
                chongfu += 1
            else:
                num = min(chongfu, A[i] - A[i - 1] - 1)
                result += ((A[i - 1] + 1) + (A[i - 1] + num)) / 2 * num
                chongfu -= num
        return int(result)


if __name__ == '__main__':
    so = Solution()
    print(so.minIncrementForUnique([3, 2, 1, 2, 1, 7]))
