from typing import List, Set


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def get_set(i, j, change_set: Set):
            use = True
            turns = ((0, 1), (1, 0), (0, -1), (-1, 0))
            for turn in turns:
                if i + turn[0] >= 0 and i + turn[0] <= m and j + turn[1] >= 0 and j + \
                        turn[1] <= n and board[i + turn[0]][j + turn[1]] == 'O' and (
                        i + turn[0], j + turn[1]) not in change_set:
                    if i + turn[0] == 0 or i + turn[0] == m or j + turn[1] == 0 or j + \
                            turn[1] == n:
                        use = False
                    change_set.add((i + turn[0], j + turn[1]))
                    next_use = get_set(i + turn[0], j + turn[1], change_set)
                    if not next_use:
                        use = next_use
            return use

        if not board:
            return
        m, n, not_change = len(board) - 1, len(board[0]) - 1, set()
        for i in range(1, m):
            for j in range(1, n):
                change_set = set()
                if board[i][j] == 'X' or (i, j) in not_change:
                    continue
                change_set.add((i, j))
                use = get_set(i, j, change_set)
                for change in change_set:
                    if use:
                        board[change[0]][change[1]] = 'X'
                    else:
                        not_change.add(change)


if __name__ == '__main__':
    so = Solution()
    re = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]
    so.solve(re)
    print(re)
