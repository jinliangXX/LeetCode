from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        lenght, result = len(nums), list()
        for num in range(2 ** lenght):
            index, now_list = 0, list()
            while num >= 1:
                if num & 1 == 1:
                    now_list.append(nums[index])
                index += 1
                num >>= 1
            result.append(now_list)
        return result


if __name__ == '__main__':
    so = Solution()
    re = so.subsets([1, 2, 3])
    print(re)
