from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n
        while left < right:
            mid = (left + right) // 2
            index_m, index_n = mid // n, mid % n
            if matrix[index_m][index_n] == target:
                return True
            elif matrix[index_m][index_n] < target:
                left = mid + 1
            else:
                right = mid
        return False


if __name__ == '__main__':
    so = Solution()
    input = [[1], [3]]
    target = 3
    print(so.searchMatrix(input, target))
