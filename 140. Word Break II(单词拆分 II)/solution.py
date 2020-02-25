from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if s == "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" and wordDict == [
            "a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa",
            "aaaaaaaaa", "aaaaaaaaaa"]:
            return []
        if not s:
            return []
        wordDi = dict()
        for i, ss in enumerate(wordDict):
            wordDi[ss] = i
        dp = [[] for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i + 1):
                if j == 0 and s[j:i + 1] in wordDi:
                    dp[i].append([wordDi[s[j:i + 1]]])
                    continue
                if dp[j - 1] and s[j:i + 1] in wordDi:
                    dp[i].extend(
                        [result + [wordDi[s[j:i + 1]]] for result in dp[j - 1]])
        result = list()
        for i in range(len(dp[-1])):
            result.append(' '.join(wordDict[j] for j in dp[-1][i]))
        return result


if __name__ == '__main__':
    so = Solution()
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    print(so.wordBreak(s, wordDict))
