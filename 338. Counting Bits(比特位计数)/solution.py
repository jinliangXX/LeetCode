from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        result = [0]
        for i in range(1, num + 1):
            result.append(result[i >> 1] + (i & 1))
        return result

if __name__ == '__main__':
    so = Solution()
    input = 5
    print(so.countBits(input))