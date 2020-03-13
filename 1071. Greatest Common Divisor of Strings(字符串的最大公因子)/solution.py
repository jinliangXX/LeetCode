import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        '''
        https://leetcode-cn.com/problems/greatest-common-divisor-of-strings/solution/zi-fu-chuan-de-zui-da-gong-yin-zi-by-leetcode-solu/
        官方题解

        :param str1:
        :param str2:
        :return:
        '''
        len_gcd = math.gcd(len(str1), len(str2))
        result = str1[:len_gcd]
        return result if result * (len(str1) // len_gcd) == str1 and result * (
                len(str2) // len_gcd) == str2 else ''


'''
min_length = min(len(str1), len(str2))
        if str1[:min_length] != str2[:min_length]:
            return ''
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        if len(str1) == len(str2):
            return str1

        def is_zhengchu(str3, result):
            if len(str3) % len(result) != 0:
                return False
            return True if str3 == result * (len(str3) // len(result)) else False

        result = str2
        while result:
            if len(str1) % len(result) == 0 and len(str2) % len(result) == 0:
                if is_zhengchu(str2, result) and is_zhengchu(str1, result):
                    return result
            result = result[:-1]
        return result

'''

if __name__ == '__main__':
    so = Solution()
    print(so.gcdOfStrings(str1="LEET", str2="CODE"))
