class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        i2, i3, i5 = 0, 0, 0

        for _ in range(n - 1):
            num = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
            nums.append(num)
            if num == nums[i2] * 2:
                i2 += 1
            if num == nums[i3] * 3:
                i3 += 1
            if num == nums[i5] * 5:
                i5 += 1
        return nums[-1]


if __name__ == '__main__':
    so = Solution()
    print(so.nthUglyNumber(10))
