from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, num in enumerate(nums):
            j = i
            while j > 0:
                if self.is_bigger(str(num),
                                  str(nums[j - 1])):
                    nums[j] = nums[j - 1]
                    j -= 1
                    if j == 0:
                        nums[j] = num
                else:
                    nums[j] = num
                    break
        result = ''
        if nums[0] == 0:
            return '0'
        for num in nums:
            result += str(num)
        return result

    def is_bigger(self, num1: str, num2: str) -> bool:
        return True if int(num1 + num2) > int(
            num2 + num1) else False


if __name__ == '__main__':
    so = Solution()
    re = so.largestNumber([3, 30, 34, 5, 9])
    print(re)
    aa = "995998549642963295795569525905189958985890288238775871870185978591838283748308308827481618052787813771758475277519744072727265721971071006861683682268046787640663256310614560285906582858175752573156385565552654905441522852245213513750414822478747104662455545424532434289408839763963946391038663723370035134023393328828692788270926232581243924362362304226421162109163016131603127210891014"
    bb = "995998549642963295795569525905189958985890288238775871870185978591838283748308830827481618052787813771758475277519744072727265721971071006861683682268046787640663256310614560285906582858175752573156385565552654905441522852245213513750414822478747104662455545424532434289408839763963946391038663723370035134023393328828692788270926232581243924362362304226421162109163016131603127210891014"
    for i, char in enumerate(aa):
        if char != bb[i]:
            print(str(i) + '：' + char)
    print(aa.index('308'))