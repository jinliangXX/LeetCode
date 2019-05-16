from typing import List


class Solution:
    def coinChange(self, coins: List[int],
                   amount: int) -> int:
        list_amount = [-1] * (amount + 1)
        list_amount[0] = 0
        for i in range(amount + 1):
            if list_amount[i] == -1:
                now = -1
                for j in range(len(coins)):
                    if coins[j] <= i and list_amount[
                        i - coins[j]] != -1:
                        now_num = list_amount[
                                      i - coins[j]] + 1
                        if now == -1:
                            now = now_num
                        elif now > now_num:
                            now = now_num
                list_amount[i] = now
        return list_amount[amount]


if __name__ == '__main__':
    so = Solution()
    result = so.coinChange([1, 2, 5], 11)
    print(result)
