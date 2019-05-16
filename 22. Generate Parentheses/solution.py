class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = list()
        for i in range(n):
            if i == 0:
                result.append('()')
                continue
            now = set()
            for str_i in result:
                now.add('(' + str_i + ')')
                index_start = 0
                for j in range(i):
                    if j == i - 1:
                        now.add(str_i + '()')
                        continue
                    index = str(str_i).index(')',
                                             index_start)
                    index_start = index + 1
                    now.add(
                        str_i[0:index + 1] + '(' + str_i[
                                                   index + 1:] + ')')
            result = list(now)
        return result


if __name__ == '__main__':
    so = Solution()
    so.generateParenthesis(3)
