from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        sum_num = sum(A)
        sum_block = sum_num / 3
        left = 0
        left_num = sum_block
        while left < len(A):
            left_num -= A[left]
            if left_num == 0:
                break
            left += 1
        right = left + 1
        while right < len(A):
            sum_block -= A[right]
            if sum_block == 0:
                break
            right += 1
        return True if right < len(A) - 1 else False


if __name__ == '__main__':
    input = [1, -1, 1, -1]
    so = Solution()
    print(so.canThreePartsEqualSum(input))
