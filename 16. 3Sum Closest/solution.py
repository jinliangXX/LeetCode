class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        num_sort = sorted(nums)
        lenght = len(num_sort)
        right = lenght - 1
        result_num = abs(
            num_sort[0] + num_sort[1] + num_sort[
                right] - target)
        result = num_sort[0] + num_sort[1] + num_sort[right]
        for i, num in enumerate(num_sort):
            left = i + 1
            right = lenght - 1
            while left < right:
                if abs(num + num_sort[left] + num_sort[
                    right] - target) < result_num:
                    result_num = abs(
                        num + num_sort[left] + num_sort[
                            right] - target)
                    result = num + num_sort[left] + \
                             num_sort[right]
                    print(
                        "result_num:{}".format(result_num))
                if num_sort[left] + num_sort[
                    right] < target - num:
                    left += 1
                elif num_sort[left] + num_sort[
                    right] > target - num:
                    right -= 1
                else:
                    return target
        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 4, 8, 16, 32, 64, 128]
    target = 82
    result = solution.threeSumClosest(nums, target)
    print("result:{}".format(result))
