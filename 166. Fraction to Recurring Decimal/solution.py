class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        first = 1
        if numerator < 0:
            numerator = -numerator
            first = -first
        if denominator < 0:
            denominator = -denominator
            first = -first
        result_one = int(numerator / denominator)
        result_two = ''
        num = numerator % denominator
        if num == 0:
            return str(first * result_one)
        nums = list()
        while num != 0:
            nums.append(num)
            num *= 10
            now = int(num / denominator)
            num = num % denominator
            result_two += str(now)
            if num in nums:
                result_two = result_two[
                             :nums.index(num)] + '(' + str(
                    result_two[nums.index(num):]) + ')'
                break
        if first == -1:
            result = '-' + str(
                result_one) + '.' + result_two
        else:
            result = str(result_one) + '.' + result_two
        return result


if __name__ == '__main__':
    print(4 / 333)


