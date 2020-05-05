import collections
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [n - 1]
        graph = [[] for _ in range(n)]
        degree = [0 for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            degree[edge[0]] += 1
            degree[edge[1]] += 1
        deque = collections.deque()
        for i, gra in enumerate(graph):
            if len(gra) == 1:
                deque.append(i)
        while n > 2:
            size = len(deque)
            for _ in range(size):
                n -= 1
                index = deque.popleft()
                degree[index] = 0
                for i in graph[index]:
                    degree[i] -= 1
                    if degree[i] == 1:
                        deque.append(i)
        return list(deque)


if __name__ == '__main__':
    so = Solution()
    n = 2
    edges = [[1, 0]]
    print(so.findMinHeightTrees(n, edges))
