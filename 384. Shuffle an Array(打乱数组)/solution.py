import random

from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.shuffle_nums = list()

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        self.shuffle_nums = list(self.nums)
        for i in range(len(self.nums)):
            index = random.randint(i, len(self.nums) - 1)
            self.shuffle_nums[i], self.shuffle_nums[index] = self.shuffle_nums[index], \
                                                             self.shuffle_nums[i]

        return self.shuffle_nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
