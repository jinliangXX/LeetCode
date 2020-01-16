import sys

if __name__ == '__main__':
    s_list = list(map(str, sys.stdin.readline().strip().split()))
    for i, s in enumerate(s_list):
        if len(s) % 2 != 0:
            s_list[i] = s[::-1]
    print(' '.join(s for s in s_list))
