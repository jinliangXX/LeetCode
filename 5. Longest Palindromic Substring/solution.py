class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        method = [[0, 1], [1, 0], [1, 1]]
        for i, char in enumerate(s):
            for met in method:
                left, right = i - met[0], i + met[1]
                while left >= 0 and right < len(s) and s[
                    left] == s[right]:
                    left -= 1
                    right += 1
                if right - left - 1 > len(result):
                    result = s[left + 1:right]
        return result


if __name__ == '__main__':
    so = Solution()
    so.longestPalindrome('cbbd')
