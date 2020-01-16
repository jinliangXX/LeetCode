import sys
from typing import List


def get_re(nows: List, ree: int, result: List[List]):
    if not nows:
        result.append(ree)
    else:
        for i, now in enumerate(nows):
            re = ree * 10 + now
            new_nows = nows.copy()
            new_nows.pop(i)
            get_re(new_nows, re, result)


def GetResult(K):
    sum_num, results = sum(K), list()
    for num in range(1, 5):
        sum_now = sum_num + num
        nows, lenght = [0 for _ in range(10)], 1
        while sum(nows) < sum_now:
            lenght_now = lenght
            while lenght_now > 9:
                nows[lenght_now % 10] += 1
                lenght_now = lenght_now // 10
            nows[lenght_now] += 1
            lenght += 1
        if sum(nows) != sum_now or len(str(lenght - 1)) != num:
            continue
        nows = [nows[i] - K[i] for i in range(10)]
        if sum(nows) != num:
            continue
        new_nows = list()
        for i, now in enumerate(nows):
            if now != 0:
                for _ in range(now):
                    new_nows.append(i)
        ree = list()
        get_re(new_nows, 0, ree)
        fil = set()
        ree.sort()
        for re in ree:
            if len(str(re)) != num:
                continue
            elif re in fil:
                continue
            else:
                results.append([lenght - 1, re])
    return results


_K = list(map(int, sys.stdin.readline().strip('\n').split()))
res = GetResult(_K)

for re in res:
    print(str(re[0]) + ' ' + str(re[1]))
# print(' '.join(str(i) for i in re))
