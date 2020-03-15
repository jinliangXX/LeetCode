from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        turns = ((0, 1), (0, -1), (1, 0), (-1, 0))
        result = 0

        def dfs(i, j):
            result = 1
            grid[i][j] = -1
            for turn in turns:
                if 0 <= i + turn[0] < len(grid) and 0 <= j + turn[1] < len(grid[i]):
                    if grid[i + turn[0]][j + turn[1]] == 1:
                        result += dfs(i + turn[0], j + turn[1])
            return result

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    result = max(result, dfs(i, j))

        return result


if __name__ == '__main__':
    so = Solution()
    input = [[0, 1], [1, 1]]
    print(so.maxAreaOfIsland(input))
