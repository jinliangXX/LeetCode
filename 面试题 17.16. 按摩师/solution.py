from typing import List


class Solution:
    def massage(self, nums: List[int]) -> int:
        dp = list()
        if not nums:
            return 0
        for i, num in enumerate(nums):
            if i == 0:
                dp.append(num)
            elif i == 1:
                dp.append(max(nums[i - 1], num))
            else:
                dp.append(max(dp[i - 1], num + dp[i - 2]))
        return dp[-1]


if __name__ == '__main__':
    so = Solution()
    input = [2, 1, 4, 5, 3, 1, 1, 3]
    print(so.massage(input))
