from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        dp = [[0 for _ in triangle] for _ in range(2)]
        now = 1
        dp[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[now][j] = dp[1 - now][j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    dp[now][j] = dp[1 - now][j - 1] + triangle[i][j]
                else:
                    dp[now][j] = min(dp[1 - now][j], dp[1 - now][j - 1]) + triangle[i][j]
            now = 1 - now
        return min(dp[1 - now])


if __name__ == '__main__':
    so = Solution()
    input = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print(so.minimumTotal(input))
