from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[i]:
                    break
                dp[i] = dp[i] or (dp[j] and s[j:i] in wordDict)
        return dp[len(s)]


if __name__ == '__main__':
    so = Solution()
    re = so.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
    print(re)
'''
        if not s:
            return True
        wordDict = set(wordDict)
        left, right, last = 0, 0, None
        while left < len(s) and right <= len(s):
            if s[left:right] in wordDict:
                last = left
                left = right
            elif right == len(s):
                if last is None:
                    return False
                else:
                    right = left
                    left = last
                    last = None
            right += 1
        return True
'''
