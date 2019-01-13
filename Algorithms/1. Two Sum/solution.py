class Solution:
    def twoSum_one(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_list = sorted(nums)
        lenght = len(num_list)
        # 计算目标值的一半
        target_num = target / 2
        left = 0
        right = 1
        result_num = list()
        for i, num in enumerate(num_list):
            if num == target_num and i + 1 < lenght:
                left = i
                right = i + 1
                break
            if num > target_num:
                left = i - 1
                right = i
                break
        while left >= 0 and right < lenght:
            if num_list[left] + num_list[right] > target:
                left -= 1
            elif num_list[left] + num_list[right] < target:
                right += 1
            else:
                result_num.append(num_list[left])
                result_num.append(num_list[right])
                break
        if len(result_num) != 2:
            return
        result = [-1, -1]
        for i, num in enumerate(nums):
            if result[0] > -1 and result[1] > -1:
                break
            if result[0] < 0 and num == result_num[0]:
                result[0] = i
                continue
            if result[1] < 0 and num == result_num[1]:
                result[1] = i
                continue
        return result

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_list = sorted(nums)
        lenght = len(num_list)
        # 计算目标值的一半
        left = 0
        right = lenght - 1
        result_num = list()
        while left < right:
            if num_list[left] + num_list[right] > target:
                right -= 1
            elif num_list[left] + num_list[right] < target:
                left += 1
            else:
                result_num.append(num_list[left])
                result_num.append(num_list[right])
                break
        if len(result_num) != 2:
            return
        result = [-1, -1]
        for i, num in enumerate(nums):
            if result[0] > -1 and result[1] > -1:
                break
            if result[0] < 0 and num == result_num[0]:
                result[0] = i
                continue
            if result[1] < 0 and num == result_num[1]:
                result[1] = i
                continue
        return result


if __name__ == '__main__':
    solution = Solution()
    test = [3, 3]
    target = 6
    print(solution.twoSum(test, target))
