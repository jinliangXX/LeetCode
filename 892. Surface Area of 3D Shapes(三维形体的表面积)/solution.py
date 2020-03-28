from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    continue
                now = grid[i][j] * 6 - (grid[i][j] - 1) * 2
                if i > 0 and grid[i - 1][j] > 0:
                    now -= min(grid[i][j], grid[i - 1][j]) * 2
                if j > 0 and grid[i][j - 1] > 0:
                    now -= min(grid[i][j], grid[i][j - 1]) * 2
                result += now
        return result


if __name__ == '__main__':
    so = Solution()
    print(so.surfaceArea([[2, 2, 2], [2, 1, 2], [2, 2, 2]]))
