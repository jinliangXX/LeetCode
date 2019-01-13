class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(' ', '')
        nums = list()
        num = 0
        fuhao = '+'
        for str in s:
            if str.isdigit():
                num = num * 10 + int(str)
            elif str == '(':
                nums.append(fuhao + str)
                fuhao = '+'
            elif str == ')':
                self.cal(nums, fuhao, num)
                num = 0
                fuhao = '+'
                while 1:
                    now = nums.pop()
                    if '-(' == now:
                        fuhao = '-'
                        break
                    elif '+(' == now:
                        break
                    else:
                        num += now
            else:
                self.cal(nums, fuhao, num)
                fuhao = str
                num = 0
        self.cal(nums, fuhao, num)
        result = 0
        for b in nums:
            result += b
        return result

    def cal(self, nums, str, num):
        return {
            '+': lambda nums, num: nums.append(int(num)),
            '-': lambda nums, num: nums.append(-int(num))
        }[str](nums, num)


if __name__ == '__main__':
    solution = Solution()
    s = "1-(5)"
    print(solution.calculate(s))
