class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_now(s: str):
            return (ord(s) >= ord('0') and ord(s) <= ord('9')) or (
                    ord(s) >= ord('a') and ord(s) <= ord('z')) or (
                           ord(s) >= ord('A') and ord(s) <= ord('Z'))

        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not is_now(s[left]):
                left += 1
            while left < right and not is_now(s[right]):
                right -= 1
            if s[left] == s[right] or (s[left].isalpha() and s[right].isalpha() and s[
                left].upper() == s[right].upper()):
                left += 1
                right -= 1
                continue
            else:
                return False
        return True


if __name__ == '__main__':
    so = Solution()
    s = "0P"
    re = so.isPalindrome(s)
    print(re)
