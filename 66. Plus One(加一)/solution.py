from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        plus = 1
        for i in range(length - 1, -1, -1):
            digits[i] += plus
            if digits[i] > 9:
                digits[i] -= 10
            else:
                plus = 0
                break
        if plus:
            digits.insert(0, plus)
        return digits
