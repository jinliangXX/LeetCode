from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        result = list()
        for num in nums:
            if not result:
                result.append(num)
                continue
            # 二分
            if num > result[-1]:
                result.append(num)
                continue
            left, right = 0, len(result)
            while left < right:
                mid = (left + right) // 2
                if result[mid] == num:
                    right = mid
                elif result[mid] > num:
                    right = mid
                else:
                    left = mid + 1
            result[left] = num
        return len(result)


if __name__ == '__main__':
    so = Solution()
    print(so.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))
