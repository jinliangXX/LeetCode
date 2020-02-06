from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        turns = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def dfs(i, j, target, board_copy, now):
            if now == len(target) - 1:
                return True
            board_copy[i][j] = '0'
            now += 1
            for turn in turns:
                if 0 <= i + turn[0] < len(board) and 0 <= j + turn[1] < len(board[0]):
                    if board_copy[i + turn[0]][j + turn[1]] == target[now]:
                        if dfs(i + turn[0], j + turn[1], target, board_copy, now):
                            return True
            board_copy[i][j] = target[now - 1]
            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if dfs(i, j, word, board.copy(), 0):
                        return True
        return False


if __name__ == '__main__':
    so = Solution()
    input = [["C","A","A"],["A","A","A"],["B","C","D"]]
    print(so.exist(input, 'AAB'))
