class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        stack = list()
        result = 0
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                    if not stack:
                        result = max(result, i + 1)
                    else:
                        result = max(result, i - stack[-1])
                else:
                    stack.append(i)

        return result


if __name__ == '__main__':
    so = Solution()
    print(so.longestValidParentheses(")()())"))
