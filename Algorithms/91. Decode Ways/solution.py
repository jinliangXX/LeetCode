class Solution:
    def numDecodings(self, s: str) -> int:
        if s is None or s[0] == '0' or '00' in s:
            return 0
        last = 1
        last_next = 1
        result = 1
        for i, char in enumerate(s):
            if i < 1:
                continue
            if char == '0':
                if int(s[i - 1] + char) > 20:
                    return 0
                result = last
            elif 9 < int(s[i - 1] + char) <= 26:
                result = last_next + last
            else:
                result = last_next
            last = last_next
            last_next = result
        return result


if __name__ == '__main__':
    so = Solution()
    re = so.numDecodings('226')
    print(re)
