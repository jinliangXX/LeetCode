from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        zimu = dict()
        zimu['2'] = ['a', 'b', 'c']
        zimu['3'] = ['d', 'e', 'f']
        zimu['4'] = ['g', 'h', 'i']
        zimu['5'] = ['j', 'k', 'l']
        zimu['6'] = ['m', 'n', 'o']
        zimu['7'] = ['p', 'q', 'r', 's']
        zimu['8'] = ['t', 'u', 'v']
        zimu['9'] = ['w', 'x', 'y', 'z']
        result = list()
        for i in digits:
            sub = zimu[i]
            now = result.copy()
            result = list()
            for j in sub:
                if len(now) > 0:
                    result.extend([c + j for c in now])
                else:
                    result.append(j)
        return result


if __name__ == '__main__':
    so = Solution()
    so.letterCombinations("23")
