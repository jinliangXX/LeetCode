from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.dp = [[0 for _ in matrix[0]] for _ in matrix]
        for i in range(len(matrix)):
            now = 0
            for j in range(len(matrix[i])):
                now += matrix[i][j]
                self.dp[i][j] = self.dp[i - 1][j] + now if i > 0 else now

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        now = self.dp[row1 - 1][col2] if row1 > 0 else 0
        now += self.dp[row2][col1 - 1] if col1 > 0 else 0
        now -= self.dp[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        return self.dp[row2][col2] - now

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
