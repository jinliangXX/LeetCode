class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        result = [[0 for col in range(n)] for row in
                  range(m)]
        for i, nums in enumerate(board):
            for j, num in enumerate(nums):
                result[i][j] = num
                if num == 0:
                    if self.cal_live_num(m, n, i, j,
                                         board) == 3:
                        result[i][j] = 1
                else:
                    if self.cal_live_num(m, n, i, j,
                                         board) < 2 or self.cal_live_num(
                        m, n, i, j, board) > 3:
                        result[i][j] = 0
        for i, nums in enumerate(result):
            for j, num in enumerate(nums):
                board[i][j] = num

    def cal_live_num(self, m, n, i, j, board):
        result = 0
        # 左面
        if j > 0 and board[i][j - 1] == 1:
            result += 1
        # 右面
        if j < n - 1 and board[i][j + 1] == 1:
            result += 1
        # 上面
        if i > 0 and board[i - 1][j] == 1:
            result += 1
        # 下面
        if i < m - 1 and board[i + 1][j] == 1:
            result += 1
        # 左上
        if j > 0 and i > 0 and board[i - 1][j - 1] == 1:
            result += 1
        # 右上
        if j < n - 1 and i > 0 and board[i - 1][j + 1] == 1:
            result += 1
        # 左下
        if j > 0 and i < m - 1 and board[i + 1][j - 1] == 1:
            result += 1
        # 右下
        if j < n - 1 and i < m - 1 and board[i + 1][
            j + 1] == 1:
            result += 1
        return result


if __name__ == '__main__':
    so = Solution()
    aa = so.gameOfLife([
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ])
    print(aa)
