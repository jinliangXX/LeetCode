import sys

if __name__ == "__main__":
    result = list()
    n = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().strip('\n').split()))
    for lenght in range(1, n + 1):
        nows, left = nums[0:lenght], 1
        while left + lenght <= len(nums):
            if sum(nums[left:left + lenght]) < sum(nows):
                nows = nums[left:left + lenght]
            left += 1
        result.append(max(nows))
    print(" ".join(str(i) for i in result))
