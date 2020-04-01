from typing import List


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        num = 0
        result = list()
        if not seq:
            return result
        for i in range(len(seq)):
            if seq[i] == '(':
                num += 1
                result.append(0 if num % 2 == 0 else 1)
            else:
                result.append(0 if num % 2 == 0 else 1)
                num -= 1
        return result


if __name__ == '__main__':
    so = Solution()
    print(so.maxDepthAfterSplit("()(())()"))
