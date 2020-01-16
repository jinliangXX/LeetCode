import sys

if __name__ == "__main__":
    result, final = 1, 1
    [n, k] = list(map(int, sys.stdin.readline().strip('\n').split()))
    for i in range(n - 1):
        if i == n - 2:
            result *= k - 2
        else:
            result *= k - 1
        if result > 1000000007:
            final *= result % 1000000007
            result = 1
            if final == 0:
                break
            if final > 1000000007:
                final = final % 1000000007
    final *= result % 1000000007
    print(final % 1000000007)
