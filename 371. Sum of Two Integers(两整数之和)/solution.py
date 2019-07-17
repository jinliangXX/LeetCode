class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 2^32
        MASK = 0x100000000
        # 整型最大值
        MAX_INT = 0x7FFFFFFF
        MIN_INT = MAX_INT + 1
        while b != 0:
            # 计算进位
            carry = (a & b) << 1
            # 取余范围限制在 [0, 2^32-1] 范围内
            a = (a ^ b) % MASK
            b = carry % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)

        # result = a ^ b
        # add = (a & b) << 1
        # while add != 0:
        #     add_new = result & add
        #     result = result ^ add
        #     add = add_new << 1
        # return result


if __name__ == '__main__':
    print(int('0x7FFFFFFF', 16))
    print(2 ** 31)
    so = Solution()
    re = so.getSum(-2, 3)
    print(re)
