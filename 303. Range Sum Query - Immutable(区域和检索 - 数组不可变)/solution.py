from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.result = list()
        last = 0
        for num in nums:
            last += num
            self.result.append(last)

    def sumRange(self, i: int, j: int) -> int:
        return self.result[j] - self.result[i - 1] if i > 0 else self.result[j]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
