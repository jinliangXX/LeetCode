from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = list()
        for i in range(1, n + 1):
            now = ''
            if i % 3 == 0:
                now += 'Fizz'
            if i % 5 == 0:
                now += 'Buzz'
            if now == '':
                result.append(str(i))
            else:
                result.append(now)
        return result
