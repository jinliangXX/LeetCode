from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dp = [[False for _ in range(target + 1)] for _ in range(len(nums) + 1)]
        dp = [[True] + i[1:] for i in dp]
        for i in range(1, len(nums) + 1):
            for j in range(1, target + 1):
                if j - nums[i - 1] < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
        return dp[-1][-1]


if __name__ == '__main__':
    so = Solution()
    print(so.canPartition([1, 2, 3, 4, 5, 6, 7]))
