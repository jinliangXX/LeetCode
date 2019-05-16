from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ''
        # 找到最小长度的字符串
        str_short = strs[0]
        for str in strs:
            if len(str) < len(str_short):
                str_short = str
        result = ''
        for i, char in enumerate(str_short):
            for j, str in enumerate(strs):
                if char != str[i]:
                    return result
            result += char
        return result
