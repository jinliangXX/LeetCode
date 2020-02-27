import math
'''
可以将特例加入字典中
更省事
'''

class Solution:
    def intToRoman(self, num: int) -> str:
        result = ''
        luoma = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        for key in sorted(luoma.keys(), reverse=True):
            while num >= key or (key > 1 and num >= key - 10 ** (
                    math.ceil(math.log(key, 10)) - 1)):
                if num >= key:
                    result += luoma[key]
                    num -= key
                else:
                    result += luoma[10 ** (math.ceil(math.log(key, 10)) - 1)] + luoma[key]
                    num -= key - 10 ** (math.ceil(math.log(key, 10)) - 1)
            if num == 0:
                return result
        return result


if __name__ == '__main__':
    so = Solution()
    print(so.intToRoman(4))
