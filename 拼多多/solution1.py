import sys

if __name__ == "__main__":
    nums_a = list(map(int, sys.stdin.readline().strip().split()))
    nums_b = list(map(int, sys.stdin.readline().strip().split()))
    index, last = None, None
    for i, num in enumerate(nums_a):
        if last is None:
            last = num
        else:
            if num > last:
                last = num
            else:
                index = i
                break
    left, tests = index - 1, list()
    for ind in [left, index]:
        if ind < 0:
            continue
        elif ind == 0 or ind == len(nums_a) - 1:
            tests.append(ind)
        else:
            num = nums_a[ind - 1] + 1
            if num < nums_a[ind + 1]:
                tests.append(ind)
    max_num = list()
    for test in tests:
        for b in nums_b:
            if (test == 0 and b < nums_a[test + 1]) or (
                    test == len(nums_a) - 1 and b > nums_a[test - 1]) or (
                    b > nums_a[test - 1] and b < nums_a[test + 1]):
                if (max_num and max_num[1] < b):
                    max_num[0], max_num[1] = test, b
                elif not max_num:
                    max_num.append(test)
                    max_num.append(b)
    if max_num:
        nums_a[max_num[0]] = max_num[1]
        print(" ".join(str(i) for i in nums_a))
    else:
        print('NO')
