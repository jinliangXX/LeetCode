class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        list_re = [True] * n
        list_re[0] = False
        list_re[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if list_re[i] == True:
                list_re[i * i:n:i] = [False] * len(
                    list_re[i * i:n:i])
        return sum(list_re)
