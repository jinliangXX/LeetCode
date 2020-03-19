import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        a_dict = collections.Counter(s)
        result = 0
        is_odd_number = False
        for char in a_dict:
            if a_dict[char] % 2 == 0:
                result += a_dict[char]
            else:
                is_odd_number = True
                result += a_dict[char] // 2 * 2
        result += 1 if is_odd_number else 0
        return result


if __name__ == '__main__':
    so = Solution()
    print(so.longestPalindrome("abccccdd"))
