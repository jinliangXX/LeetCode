from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = list()
        if not nums:
            return dp
        for i, num in enumerate(nums):
            dp.append([num])
            for j in range(i):
                if num % nums[j] == 0 and len(dp[j]) >= len(dp[-1]):
                    dp[-1] = dp[j] + [num]
        return max(dp, key=len)


if __name__ == '__main__':
    so = Solution()
    print(so.largestDivisibleSubset([1, 2, 3]))
