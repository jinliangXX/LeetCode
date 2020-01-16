class Solution:
    def isValid(self, s: str) -> bool:
        nows = {')': '(', '}': '{', ']': '['}
        stack = list()
        for char in s:
            if char in nows:
                if stack and stack.pop() == nows[char]:
                    continue
                else:
                    return False
            else:
                stack.append(char)
        return False if stack else True


if __name__ == '__main__':
    s = "()[]{}"
    so = Solution()
    re = so.isValid(s)
    print(re)
