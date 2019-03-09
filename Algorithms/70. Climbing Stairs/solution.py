class Solution:
    def climbStairs(self, n: int) -> int:
        last_two = 1
        last_one = 2
        if n < 3:
            return n
        for i in range(n + 1):
            if i < 3:
                continue
            num = last_two + last_one
            last_two = last_one
            last_one = num
        return num

    def cal_num(self, n):
        if n == 1 or n == 2 or n == 3:
            return n
        else:
            return self.cal_num(n - 1) + self.cal_num(n - 2)


if __name__ == '__main__':
    sol = Solution()
    print(sol.climbStairs(44))
