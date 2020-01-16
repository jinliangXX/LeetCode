from typing import List

'''
动态规划+贪婪算法
'''


class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums or len(nums) <= 1:
            return 0
        index, result = 0, 0
        while index < len(nums):
            if index + nums[index] >= len(nums) - 1:
                return result + 1
            max_now = 0
            for i in range(index, index + nums[index] + 1):
                if i + nums[i] > max_now:
                    max_now = i + nums[i]
                    index = i
            # now = [i + num for i, num in enumerate(nums[index:index + nums[index] + 1])]
            # index_now = now.index(max(now))
            result += 1
        return result


if __name__ == '__main__':
    so = Solution()
    input = [2, 3, 1, 1, 4]
    print(so.jump(input))

'''

result = [float(0) for _ in range(len(nums))]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == 0:
                result[i] = float('inf')
                continue
            now = min(result[i + 1:i + nums[i] + 1]) + 1
            result[i] = now
        return int(result[0])
'''
