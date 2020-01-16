from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nine = set()
        # 判断每一行
        for row in board:
            nine.clear()
            for char in row:
                if char != '.':
                    if char in nine:
                        return False
                    else:
                        nine.add(char)
        # 判断每一列
        for column in range(9):
            nine.clear()
            for row in board:
                if row[column] != '.':
                    if row[column] in nine:
                        return False
                    else:
                        nine.add(row[column])
        # 判断每个9宫格
        starts = ((0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6))
        for start in starts:
            (i, j) = start
            nine.clear()
            for row in range(i, i + 3):
                for column in range(j, j + 3):
                    if board[row][column] != '.':

                        if board[row][column] in nine:
                            return False
                        else:
                            nine.add(board[row][column])
        return True
