from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        row = len(matrix)
        now = 0
        while row > 1:
            for i in range(row - 1):
                now_num = matrix[now][now + i]
                matrix[now + i][now + row - 1], now_num = now_num, matrix[now + i][
                    now + row - 1]
                matrix[now + row - 1][now + row - 1 - i], now_num = now_num, \
                                                                    matrix[
                                                                        now + row - 1][
                                                                        now + row - 1 - i]
                matrix[now + row - 1 - i][now], now_num = now_num, \
                                                          matrix[now + row - 1 - i][now]
                matrix[now][now + i] = now_num
            now += 1
            row -= 2


if __name__ == '__main__':
    so = Solution()
    re = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    so.rotate(re)
    print(re)
