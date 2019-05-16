class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 二分法
        k -= 1
        left = 0
        right = len(nums) - 1
        index = self.cal_nums(nums, left, right)
        while True:
            if index < k:
                left = index + 1
                index = self.cal_nums(nums, left, right)
            elif index > k:
                right = index - 1
                index = self.cal_nums(nums, left, right)
            else:
                break
        return nums[k]

    def cal_nums(self, nums, left, right):
        num = nums[left]
        now = 1
        index = left
        while left <= right:
            if now == 1:
                if nums[right] <= num:
                    right -= 1
                    now = 1
                else:
                    nums[index] = nums[right]
                    now = 0
                    index = right
                    left += 1
            else:
                if nums[left] > num:
                    left += 1
                    now = 0
                else:
                    nums[index] = nums[left]
                    now = 1
                    index = left
                    right -= 1
        nums[index] = num
        return index


if __name__ == '__main__':
    so = Solution()
    so.findKthLargest([3, 2, 1, 5, 6, 4], 2)

'''
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 初始化大顶堆
        self.cal_nums(nums)
        result = nums[0]
        for i in range(1, k):
            nums[0] = nums[len(nums) - 1]
            nums.pop()
            # 重新生成大顶堆
            self.cal_nums(nums)
            result = nums[0]
        return result

    def cal_nums(self, nums):
        for i in range(int((len(nums) - 2) / 2), -1, -1):
            index = 2 * i + 1
            num = nums[2 * i + 1]
            if index + 1 < len(nums) and nums[
                index + 1] > num:
                index += 1
                num = nums[index]
            if nums[i] < num:
                now = nums[i]
                nums[i] = num
                nums[index] = now
'''
