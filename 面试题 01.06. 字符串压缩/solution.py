class Solution:
    def compressString(self, S: str) -> str:
        left, right = 0, 0
        result = ''
        while right < len(S):
            while right < len(S) and S[right] == S[left]:
                right += 1
            result += S[left] + str(right - left)
            left = right
        return result if len(result) < len(S) else S


if __name__ == '__main__':
    so = Solution()
    print(so.compressString("abbccd"))
