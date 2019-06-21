class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        count = 32
        while count:
            result <<= 1
            result += n & 1
            n >>= 1
            count -= 1

        return result


'''
s = bin(n)
        s = s[2:]
        s = s[::-1]
        s += '0' * (32 - len(s))
        return int(s, 2)
'''

if __name__ == '__main__':
    so = Solution()
    re = so.reverseBits(43261596)
    print(re)
