import sys

if __name__ == "__main__":
    [n, q] = list(map(int, sys.stdin.readline().strip('\n').split()))
    nums = list(map(int, sys.stdin.readline().strip('\n').split()))
    for _ in range(q):
        result = 0
        ope = int(sys.stdin.readline().strip())
        for i in range(n):
            if ope <= nums[i]:
                nums[i] -= 1
                result += 1
        print(result)
