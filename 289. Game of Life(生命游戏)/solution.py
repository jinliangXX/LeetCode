from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        turns = ((0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (-1, -1), (1, -1), (1, 1))

        def change(i, j):
            live_number = 0
            for turn in turns:
                if 0 <= i + turn[0] < len(board) and 0 <= j + turn[1] < len(board[0]) and \
                        board[i + turn[0]][j + turn[1]] in (1, 4):
                    live_number += 1
            if board[i][j] == 0:
                if live_number == 3:
                    board[i][j] = 3
            else:
                if live_number not in (2, 3):
                    board[i][j] = 4

        for i in range(len(board)):
            for j in range(len(board[i])):
                change(i, j)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 3:
                    board[i][j] = 1
                if board[i][j] == 4:
                    board[i][j] = 0


if __name__ == '__main__':
    so = Solution()
    input = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    print(so.gameOfLife(input))
