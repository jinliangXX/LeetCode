class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def isMatch(i: int, j: int, last: str, num: int):
            if i >= len(s):
                return True
            if j >= len(p):
                return False
            if p[j] == '*':
                if last == '*' or s[i] == last:
                    now_result = False
                    now_result = now_result or isMatch(i + 1, j + 1, s[i], num)
                    for now_id in range(1, num + 1):
                        if s[i + now_id] == s[i]:
                            now_result = now_result or isMatch(i + 1 + now_id,
                                                               j + 1 + now_id, s[i],
                                                               num - now_id)
                        else:
                            break
                    return now_result
                else:
                    return False
            else:
                if s[i] == p[j] or p[j] == '.':
                    return isMatch(i + 1, j + 1, s[i], num)
                else:
                    return False

        lenght = len(s) - len(p)
        result = isMatch(0, 0, '*', lenght)
        return result


if __name__ == '__main__':
    so = Solution()
    re = so.isMatch("ab", ".*")
    print(re)
