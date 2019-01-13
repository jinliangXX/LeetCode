class Solution:
    def calculate_one(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(' ', '')
        num_list = list()
        yunsuan = ['*', '/', '+', '-']
        num = 0
        for str in s:
            if str in yunsuan:
                num_list.append(num)
                num_list.append(str)
                num = 0
            else:
                num = 10 * num + int(str)
        num_list.append(num)
        a = 0
        b = 0
        str_first = ['*', '/']
        while len(num_list) > 2:
            index = 0
            if len(num_list) > 3 and num_list[
                index + 1] not in str_first and num_list[
                index + 3] in str_first:
                index += 2
            a = num_list[index]
            b = num_list[index + 2]
            fuhao = num_list[index + 1]
            num = self.get_num(a, b, fuhao)
            num_list.pop(index)
            num_list.pop(index)
            num_list.pop(index)
            # num_list[index:].remove(int(a))
            # num_list[index:].remove(fuhao)
            # num_list[index:].remove(int(b))
            num_list.insert(index, num)
        return num_list[0]

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(' ', '')
        num_list = list()
        result = 0
        num = 0
        fuhao = '+'
        for str in s:
            if not str.isdigit():
                self.cal_num(num, num_list, fuhao)
                fuhao = str
                num = 0
            else:
                num = 10 * num + int(str)
        self.cal_num(num, num_list, fuhao)
        for numb in num_list:
            result += numb
        return result

    def cal_num(self, x, num_list, fuhao):
        '''

        :param x:
        :param num_list:
        :param fuhao:
        :return:
        '''
        return {
            '+': lambda x, num_list: num_list.append(x),
            '-': lambda x, num_list: num_list.append(-x),
            '*': lambda x, num_list: num_list.append(
                num_list.pop() * x),
            '/': lambda x, num_list: num_list.append(
                int(num_list.pop() / x))
        }[fuhao](x, num_list)

    def get_num(self, a, b, fuhao):
        '''
        计算
        :param a:
        :param b:
        :param fuhao:
        :return:
        '''
        a = int(a)
        b = int(b)
        return {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)
        }[fuhao](a, b)


if __name__ == '__main__':
    solution = Solution()
    s = '12-3*4'
    result = solution.calculate(s=s)
    print(result)
