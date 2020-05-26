class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        result, num = 1, 0
        for i in range(1, n + 1):
            if i == 1:
                num = (11 - i)
                result = result * num
            elif i == 2:
                num = (11 - i) ** 2
                result += num
            elif i < 11:
                num *= (11 - i)
                result += num
            else:
                return result
        return result

if __name__ == '__main__':
    so = Solution()
    print(so.countNumbersWithUniqueDigits(3))