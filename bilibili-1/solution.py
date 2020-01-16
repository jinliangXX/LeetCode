import sys


class Solution:
    def get_num(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 10:
            return 1
        s = str(n)
        now, last, last_last = 0, 1, 1
        for i, char in enumerate(s):
            if i < 1:
                continue
            if char == '0':
                if int(s[i - 1] + char) <= 26 and int(s[i - 1] + char) > 9:
                    now += max(1, last_last)
                else:
                    now = 0
            else:
                now = last
                if int(s[i - 1] + char) <= 26 and int(s[i - 1] + char) > 9:
                    now += max(1, last_last)
            last_last = last
            last = now
        return now


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip('\n'))
    so = Solution()
    print(so.get_num(n))
