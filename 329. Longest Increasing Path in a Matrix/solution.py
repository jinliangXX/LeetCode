from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[
        List[int]]) -> int:
        map_list = dict()
        global m
        m = len(matrix)
        if m == 0:
            return 0
        global n
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                index = str(i) + ':' + str(j)
                if index in map_list:
                    continue
                map_list[index] = 1
                self.cal_num(i, j, matrix, map_list,
                             [index])
        result = 0
        for i in range(m):
            for j in range(n):
                index = str(i) + ':' + str(j)
                if map_list[index] > result:
                    result = map_list[index]

        return result

    def cal_num(self, i, j, matrix, map_list, list_now):
        num = matrix[i][j]
        # left
        if j > 0:
            now_index = j - 1
            left = matrix[i][now_index]
            if left > num:
                if str(i) + ':' + str(
                        now_index) in map_list:
                    next_num = map_list[
                        str(i) + ':' + str(now_index)]
                    for k, name in enumerate(list_now[::-1]):
                        if next_num + k + 1 > map_list[
                            name]:
                            map_list[
                                name] = next_num + k + 1
                else:
                    now = list()
                    now.extend(list_now)
                    now.append(
                        str(i) + ':' + str(now_index))
                    for k, name in enumerate(now[::-1]):
                        if k == 0:
                            map_list[name] = k + 1
                        if k + 1 > map_list[name]:
                            map_list[name] = k + 1
                    self.cal_num(i, now_index, matrix,
                                 map_list, now)
        if j < n - 1:
            now_index = j + 1
            right = matrix[i][now_index]
            if right > num:

                if str(i) + ':' + str(
                        now_index) in map_list:
                    next_num = map_list[
                        str(i) + ':' + str(now_index)]
                    for k, name in enumerate(list_now[::-1]):
                        if next_num + k + 1 > map_list[
                            name]:
                            map_list[
                                name] = next_num + k + 1

                else:
                    now = list()
                    now.extend(list_now)
                    now.append(
                        str(i) + ':' + str(now_index))
                    for k, name in enumerate(now[::-1]):
                        if k == 0:
                            map_list[name] = k + 1
                        if k + 1 > map_list[name]:
                            map_list[name] = k + 1
                    self.cal_num(i, now_index, matrix,
                                 map_list, now)
        if i > 0:
            now_index = i - 1
            up = matrix[now_index][j]
            if up > num:
                now = list()
                now.extend(list_now)
                if str(now_index) + ':' + str(
                        j) in map_list:
                    next_num = map_list[
                        str(now_index) + ':' + str(j)]
                    for k, name in enumerate(list_now[::-1]):
                        if next_num + k + 1 > map_list[
                            name]:
                            map_list[
                                name] = next_num + k + 1
                else:
                    now = list()
                    now.extend(list_now)
                    now.append(
                        str(now_index) + ':' + str(j))
                    for k, name in enumerate(now[::-1]):
                        if k == 0:
                            map_list[name] = k + 1
                        if k + 1 > map_list[name]:
                            map_list[name] = k + 1
                    self.cal_num(now_index, j, matrix,
                                 map_list, now)
        if i < m - 1:
            now_index = i + 1
            down = matrix[now_index][j]
            if down > num:

                if str(now_index) + ':' + str(
                        j) in map_list:
                    next_num = map_list[
                        str(now_index) + ':' + str(j)]
                    for k, name in enumerate(list_now[::-1]):
                        if next_num + k + 1 > map_list[
                            name]:
                            map_list[
                                name] = next_num + k + 1
                else:
                    now = list()
                    now.extend(list_now)
                    now.append(
                        str(now_index) + ':' + str(j))
                    for k, name in enumerate(now[::-1]):
                        if k == 0:
                            map_list[name] = k + 1
                        if k + 1 > map_list[name]:
                            map_list[name] = k + 1
                    self.cal_num(now_index, j, matrix,
                                 map_list, now)

#
# if __name__ == '__main__':
#     matrix = [
#         [9, 9, 4],
#         [6, 6, 8],
#         [2, 1, 1]
#     ]
#     so = Solution()
#     so.longestIncreasingPath(matrix)
