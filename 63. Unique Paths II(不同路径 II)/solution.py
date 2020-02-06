from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        size, result = len(obstacleGrid), list()
        for i in obstacleGrid[0]:
            if i == 0 and (not result or result[-1] == 1):
                result.append(1)
            else:
                result.append(0)
        for i in range(1, len(obstacleGrid)):
            if obstacleGrid[i][0] == 0 and result[0] == 1:
                result[0] = 1
            else:
                result[0] = 0
            for j in range(1, len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 0:
                    result[j] = result[j] + result[j - 1]
                else:
                    result[j] = 0
        return result[-1]


if __name__ == '__main__':
    input = [[1],[0]]
    so = Solution()
    print(so.uniquePathsWithObstacles(input))
