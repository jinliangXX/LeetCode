import sys

if __name__ == "__main__":
    result = list()
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().strip('\n').split()))
    total = n + 1
    for num in nums:
        result.append(total - num)
    print(" ".join(str(i) for i in result))
