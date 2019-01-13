class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        num_sort = sorted(nums)
        lenght = len(num_sort) - 1
        right = lenght
        result = self.nSum(4, num_sort, 0, right, target,
                           lenght, [])
        return result

    def nSum(self, N, num_sort, left, right, target,
             lenght, result_ago):
        result = list()
        if N == 2:
            begin = left
            while left < right:
                if right < lenght and num_sort[right] == \
                        num_sort[right + 1]:
                    right -= 1
                    continue
                if left > begin and num_sort[left] == \
                        num_sort[
                            left - 1]:
                    left += 1
                    continue
                if num_sort[left] + num_sort[
                    right] < target:
                    left += 1
                elif num_sort[left] + num_sort[
                    right] > target:
                    right -= 1
                else:
                    result.append(
                        result_ago + [num_sort[left],
                                      num_sort[right]])
                    right -= 1
            return result
        else:
            if right - left + 1 < N or target < num_sort[
                left] * N or target > num_sort[right] * N:
                return result
            for i, num in enumerate(num_sort):
                if i < left or (i > left and num_sort[
                    i - 1] == num):
                    continue
                result_item = self.nSum(N - 1, num_sort,
                                        i + 1,
                                        right, target - num,
                                        lenght,
                                        result_ago + [num])
                if len(result_item) > 0:
                    result.extend(result_item)
            return result


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    solution = Solution()
    print(solution.fourSum(nums, target))
