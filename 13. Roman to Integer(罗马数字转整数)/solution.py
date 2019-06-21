class Solution:
    def romanToInt(self, s: str) -> int:
        luo = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i, char in enumerate(s):
            if i + 1 < len(s) and luo[char] < luo[s[i + 1]]:
                result -= luo[char]
            else:
                result += luo[char]
        return result


if __name__ == '__main__':
    so = Solution()
    re = so.romanToInt("MCMXCIV")
    print(re)
