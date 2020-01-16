import sys
from typing import List


class Solution:

    def get_pic(self, h: int, w: int, p: List, m: int, k: List):
        result = [[None for _ in range(h - m + 1)] for _ in range(h - m + 1)]
        for i in range(h - m + 1):
            for j in range(h - m + 1):
                list_t = [p[i][j:j + m] for i in range(i, i + m)]
                now = 0
                for ii in range(m):
                    for jj in range(m):
                        now += list_t[ii][jj] * k[ii][jj]
                # now = sum(k * list_t)
                result[i][j] = min(255, int(now))
        return result


if __name__ == '__main__':
    [h, w] = list(map(int, sys.stdin.readline().strip().split()))
    p = list()
    for _ in range(h):
        p.append(list(map(int, sys.stdin.readline().strip().split())))
    m = int(sys.stdin.readline().strip('\n'))
    k = list()
    for _ in range(m):
        k.append(list(map(float, sys.stdin.readline().strip().split())))
    so = Solution()
    result = so.get_pic(h, w, p, m, k)
    for re in result:
        print(' '.join(str(i) for i in re))
