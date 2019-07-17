class Solution:
    def myAtoi(self, str: str) -> int:
        result = None
        if not str:
            return 0
        str, isFu, max_num = str.lstrip(), False, 2 ** 31 // 10
        for char in str:
            if result is None:
                if char == '+':
                    result = 0
                elif char == '-':
                    result = 0
                    isFu = True
                elif char in ('0,1,2,3,4,5,6,7,8,9'):
                    result = int(char)
                else:
                    return 0
            else:
                if char in ('0,1,2,3,4,5,6,7,8,9'):
                    if (isFu and result > max_num) or (
                            isFu and result == max_num and int(char) > 8):
                        return -2 ** 31
                    elif (not isFu and result > max_num) or (
                            not isFu and result == max_num and int(char) > 7):
                        return 2 ** 31 - 1
                    else:
                        result = result * 10 + int(char)
                else:
                    return result if not isFu else -result
        result = 0 if result is None else result
        return result if not isFu else -result


if __name__ == '__main__':
    so = Solution()
    re = so.myAtoi("2147483646")
    print(re)
