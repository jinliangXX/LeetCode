# coding=utf-8
import sys

if __name__ == "__main__":
    # 读取第一行的n
    [n, m] = list(map(int, sys.stdin.readline().strip().split()))
    times = list(map(int, sys.stdin.readline().strip().split()))
    rele = dict()
    for i in range(m):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        if values[1] in rele:
            rele[values[1]].append(values[0])
        else:
            rele[values[1]] = [values[0]]
    results, nows, nums = list(), list(), [i for i in range(n)]
    while len(results) < n:
        new_nums = list()
        for j, index in enumerate(nums):
            if index + 1 not in rele:
                if not nows:
                    nows.append(index)
                    continue
                for i, now in enumerate(nows):
                    if times[index] < times[now] or (
                            times[index] == times[now] and index < now):
                        nows.insert(i, index)
                        break
                nows.append(index)

            else:
                new_nums.append(index)
        nums = new_nums
        index = nows.pop(0) + 1
        results.append(index)
        keys = list(rele.keys())
        for j in keys:
            if rele[j] == [index]:
                rele.pop(j)
            elif index in rele[j]:
                rele[j].remove(index)
    print(" ".join(str(i) for i in results))
