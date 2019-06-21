from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def add_next(j, now, result, s_char):
            if j < 0:
                now.append([s_char])
                return
            for index in range(len(result[j])):
                now.append(result[j][index].copy())
                now[-1].append(s_char)
        result = list()
        for i, char in enumerate(s):
            now = list()
            if result:
                add_next(i - 1, now, result, char)
                left, right = i - 1, i
                while left >= 0:
                    if s[left] == s[right]:
                        mid = (left + right) // 2
                        if (left + right) % 2 == 0 and s[left:mid] == s[mid + 1:right + 1][::-1]:
                            add_next(left - 1, now, result, s[left:right + 1])
                        if (left + right) % 2 != 0 and s[left:mid + 1] == s[mid + 1:right + 1][::-1]:
                            add_next(left - 1, now, result, s[left:right + 1])
                    left -= 1
            else:
                now.append([char])
            result.append(now)
        return result[len(s) - 1]


if __name__ == '__main__':
    so = Solution()
    re = so.partition("cdd")
