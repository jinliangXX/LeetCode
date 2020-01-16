from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n <= 0:
            return list()
        result = [[0 for _ in range(n)] for _ in range(n)]
        i, j = 0, 0
        turns = ((0, 1), (1, 0), (0, -1), (-1, 0))
        turn = 0
        for k in range(1, n ** 2 + 1):
            result[i][j] = k
            if n - 1 < i + turns[turn][0] or i + turns[turn][0] < 0 or j + turns[turn][
                1] < 0 or j + turns[turn][1] > n - 1 or result[i + turns[turn][0]][
                j + turns[turn][1]] != 0:
                if turn == 3:
                    turn = 0
                else:
                    turn += 1
            i += turns[turn][0]
            j += turns[turn][1]
        return result


if __name__ == '__main__':
    so = Solution()
    print(so.generateMatrix(3))
