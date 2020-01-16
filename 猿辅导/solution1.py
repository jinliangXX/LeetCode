import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        result, num = list(), None
        s = sys.stdin.readline().strip()
        for char in s:
            if char.isdigit():
                if num is not None:
                    num = num * 10 + int(char)
                else:
                    num = int(char)
            else:
                if num is not None:
                    now = ''
                    if result[-1] == ')':
                        result.pop()
                        while result[-1] != '(':
                            now = result.pop() + now
                        result.pop()
                    else:
                        now = result.pop()
                    result.append(now * num)
                    num = None
                result.append(char)
        if num is not None:
            now = ''
            if result[-1] == ')':
                result.pop()
                while result[-1] != '(':
                    now = result.pop() + now
                result.pop()
            else:
                now = result.pop()
            result.append(now * num)
        print(''.join(s for s in result))
