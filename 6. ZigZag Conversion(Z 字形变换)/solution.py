import math


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = ''
        if not s:
            return result
        if numRows <= 1:
            return s
        length = 2 * numRows - 2
        for i in range(numRows):
            for j in range(math.ceil(len(s) / length)):
                if i + j * length < len(s):
                    result += s[i + j * length]
                if i + j * length < i + j * length + (length - 2 * i) < len(
                        s) and length - 2 * i < length:
                    result += s[i + j * length + (length - 2 * i)]
        return result


if __name__ == '__main__':
    so = Solution()
    print(so.convert('LEETCODEISHIRING', 3))
