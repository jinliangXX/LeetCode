from typing import List


class Solution:
    def findOrder(self, numCourses: int,
                  prerequisites: List[List[int]]) -> List[
        int]:
        a = [[] for _ in range(numCourses)]
        b = [0] * numCourses
        for i, j in prerequisites:
            a[j].append(i)
            b[i] += 1
        c = [i for i in range(numCourses) if b[i] == 0]
        for i in c:
            for j in a[i]:
                b[j] -= 1
                if b[j] == 0:
                    c.append(j)
        return c if len(c) == numCourses else []


if __name__ == '__main__':
    so = Solution()
    re = so.canFinish(8, [[1, 0], [2, 6], [1, 7], [6, 4],
                          [7, 0], [0, 5]])
    print(re)
