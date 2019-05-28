from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(a, b):
            # a作为除数 必须大于b
            a, b = (a, b) if a >= b else (b, a)
            while b:
                a, b = b, a % b
            return a
        length = len(points)
        if length < 3:
            return length
        result_dict = dict()
        for i, point in enumerate(points):
            [x_1, y_1] = point
            for j in range(length):
                if i == j:
                    continue
                [x_2, y_2] = points[j]
                if x_1 == x_2:
                    index = 'y/' + str(x_1)
                else:
                    now = gcd((y_1 - y_2), (x_1 - x_2))
                    w = (y_1 - y_2) / (x_1 - x_2)
                    b = y_1 - w * x_1
                    index = str(
                        (y_1 - y_2) / now) + '/' + str(
                        (x_1 - x_2) / now) + ':' + str(b)
                if index not in result_dict:
                    result_dict[index] = set()
                result_dict[index].add(i)
                result_dict[index].add(j)
        result = 0
        for index in result_dict:
            if len(result_dict[index]) > result:
                result = len(result_dict[index])
        return result




if __name__ == '__main__':
    so = Solution()
    re = so.maxPoints([[0, 0], [94911151, 94911150],
                       [94911152, 94911151]])
    print(re)
