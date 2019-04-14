class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        fuhao = 0
        if dividend < 0:
            dividend = -dividend
            fuhao += 1
        if divisor < 0:
            fuhao += 1
            divisor = -divisor
        result = ''
        div = ''
        for i, char in enumerate(str(dividend)):
            a, b = self.cal(int(div + char), divisor)
            result += str(a)
            div = str(b)
        result = int(result)
        if fuhao == 1:
            result = -result
            if result < -2 ** 31:
                return -2 ** 31
        if result > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return result

    def cal(self, dividend: int, divisor: int):
        result = 0
        cal = 0
        while cal < dividend:
            cal += divisor
            result += 1
        if cal == dividend:
            return result, 0
        return result - 1, dividend - cal + divisor


if __name__ == '__main__':
    so = Solution()
    print(so.divide(1004958205, -2137325331))
