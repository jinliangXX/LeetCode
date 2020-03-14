from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        d = [0, nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > d[-1]:
                d.append(nums[i])
            else:
                left, right = 1, len(d)
                index = 1
                while left < right:
                    mid = (left + right) // 2
                    if d[mid] == nums[i]:
                        index = mid
                        break
                    elif d[mid] < nums[i]:
                        index = mid + 1
                        left += 1
                    else:
                        index = mid
                        right -= 1
                d[index] = nums[i]
        return len(d) - 1


'''
        if len(nums) == 0:
            return 0
        map_list = dict()
        result = 0
        for i, num in enumerate(nums[::-1]):
            index = len(nums) - i - 1
            now = 0
            for j, num_num in enumerate(nums[index + 1:]):
                if num_num > num:
                    now = max(now,
                              map_list[index + 1 + j] + 1)
            map_list[index] = now
            result = max(result, now)
        return result + 1
'''

if __name__ == '__main__':
    so = Solution()
    print(so.lengthOfLIS([4,10,4,3,8,9]))

