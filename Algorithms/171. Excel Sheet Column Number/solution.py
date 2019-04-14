class Solution:
    def titleToNumber(self, s: str) -> int:
        list_a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                  'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                  'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                  'Y', 'Z']
        result = 0
        if s is None:
            return result
        for i, char in enumerate(s):
            index = list_a.index(char)
            result += 26 ** (len(s) - i - 1) * (index + 1)
        return result


if __name__ == '__main__':
    so = Solution()
    print(so.titleToNumber('ZY'))
