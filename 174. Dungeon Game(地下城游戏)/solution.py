from typing import List
'''
正向的DP不通

需要逆向的DP
'''

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon:
            return 1
        dp = [[0 for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]
        dp[-1][-1] = max(1, 1 - dungeon[-1][-1])
        for i in range(len(dungeon) - 1, -1, -1):
            for j in range(len(dungeon[i]) - 1, -1, -1):
                last = (0, 0)
                if i == len(dungeon) - 1 and j == len(dungeon[i]) - 1:
                    continue
                elif j == len(dungeon[i]) - 1:
                    last = dp[i + 1][j]
                elif i == len(dungeon) - 1:
                    last = dp[i][j + 1]
                else:
                    last = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(1, last - dungeon[i][j])
        return dp[0][0]


if __name__ == '__main__':
    so = Solution()
    input = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    print(so.calculateMinimumHP(input))
