import sys

if __name__ == '__main__':
    # [n, q] = list(map(int, sys.stdin.readline().strip().split()))
    # s = list(map(str, sys.stdin.readline().strip().split()))
    # s_dict = dict()
    # for ss in s:
    #     sort_ss = "".join((lambda x: (x.sort(), x)[1])(list(ss)))
    #     s_dict[sort_ss] = s_dict.get(sort_ss, 0) + 1
    # for _ in range(q):
    #     query = sys.stdin.readline().strip('\n')
    #     query = "".join((lambda x: (x.sort(), x)[1])(list(query)))
    #     print(s_dict.get(query, 0))
    a = float(2 ** 63)
    print(a)