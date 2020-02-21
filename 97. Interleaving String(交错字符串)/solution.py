class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        dp = [[False for _ in range(len(s1) + 1)]
              for _ in range(len(s3) + 1)]
        dp[0][0] = True
        for length in range(1, len(s3) + 1):
            for i in range(min(len(s1) + 1, length + 1)):
                now = False
                if i != 0:
                    now = now or (dp[length - 1][i - 1] and s1[i - 1] == s3[length - 1])
                if 0 < length - i < len(s2) + 1:
                    now = now or (dp[length - 1][i] and s2[length - i - 1] == s3[
                        length - 1])
                dp[length][i] = now
        return dp[-1][-1]


if __name__ == '__main__':
    so = Solution()
    print(so.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
