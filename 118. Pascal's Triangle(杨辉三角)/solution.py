from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return list()
        result = [[1]]
        left, right = 0, 0
        for i in range(1, numRows):
            now = list()
            now.append(left + result[i - 1][0])
            for j in range(len(result[i - 1])):
                if j + 1 == len(result[i - 1]):
                    now.append(result[i - 1][j] + right)
                    continue
                now.append(result[i - 1][j] + result[i - 1][j + 1])
            result.append(now)
        return result
