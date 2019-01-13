class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        nums = list()
        s = 'sss'
        for s in tokens:
            if s not in ['+', '-', '*', '/']:
                nums.append(int(s))
            else:
                num2 = nums.pop()
                num1 = nums.pop()
                nums.append(self.cal(s, num1, num2))
        return nums[0]

    def cal(self, s, num1, num2):
        return {
            '+': lambda sum1, sum2: sum1 + sum2,
            '-': lambda sum1, sum2: sum1 - sum2,
            '*': lambda sum1, sum2: sum1 * sum2,
            '/': lambda sum1, sum2: int(sum1 / sum2)
        }[s](num1, num2)


if __name__ == '__main__':
    s = ["10", "6", "9", "3", "+", "-11", "*", "/", "*",
         "17", "+", "5", "+"]
    solution = Solution()
    print(solution.evalRPN(s))
