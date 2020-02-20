class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        l = len(s1)
        if l != len(s2): return False
        dp = [[None for _ in range(l)] for _ in range(l)]
        for i in range(l):
            for j in range(l):
                dp[i][j] = [False] * (min(l-i, l-j)+1)
        for i in range(l):
            for j in range(l):
                dp[i][j][1] = s1[i] == s2[j]
        for length in range(2, l+1):
            for i in range(l-length+1):
                for j in range(l-length+1):
                    for sep in range(1, length): # 检查每一种子串划分的方法， sep 是分割的点
                        if dp[i][j][sep] and dp[i+sep][j+sep][length - sep]:      # 当前层两个子串未经过交换的情况
                            dp[i][j][length] = True
                            break
                        if dp[i][j+length-sep][sep] and dp[i+sep][j][length-sep]: # 当前层的两个子串经过交换的情况
                            dp[i][j][length] = True
                            break
        return dp[0][0][l]
