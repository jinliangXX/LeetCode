from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [[0, 0] for _ in nums]
        for i, num in enumerate(nums):
            if i == 0:
                dp[i] = [num, 0]
            elif i == 1:
                dp[i] = [max(dp[i - 1][0], num), num]
            elif i == len(nums) - 1:
                dp[i] = [dp[i - 1][0], max(num + dp[i - 2][1], dp[i - 1][1])]
            else:
                dp[i] = [max(num + dp[i - 2][0], dp[i - 1][0]),
                         max(num + dp[i - 2][1], dp[i - 1][1])]
        return max(dp[-1])


if __name__ == '__main__':
    so = Solution()
    input = [1, 2, 3, 1]
    print(so.rob(input))
