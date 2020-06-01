class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left, right = 0, 0
        while left < len(s) and right < len(t):
            while right < len(t) and s[left] != t[right]:
                right += 1
            if right < len(t) and s[left] == t[right]:
                left += 1
                right += 1
        return True if left >= len(s) else False


if __name__ == '__main__':
    so = Solution()
    print(so.isSubsequence("abc","ahbgdc"))
