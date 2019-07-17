from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        def takeSecond(elem):
            return elem[0]

        result = list()
        if not buildings:
            return result
        nows = list()
        for build in buildings:
            nows.append([build[0], build[2]])
            nows.append([build[1], -build[2]])
        nows.sort(key=takeSecond)
        heights = list()
        for now in nows:
            if now[1] < 0:
                heights.remove(-now[1])
            if now[1] > 0:
                heights.append(now[1])
            height = max(heights) if heights else 0
            if not result or (result[-1][1] != height and result[-1][0] < now[0]):
                result.append([now[0], height])
            elif result[-1][1] != height and result[-1][0] == now[0]:
                result[-1] = [now[0], height]
                if len(result) > 1 and result[-1][1] == result[-2][1]:
                    result.pop(-1)
        return result


if __name__ == '__main__':
    a = [[0, 2, 3], [2, 5, 3]]
    so = Solution()
    re = so.getSkyline(a)
    print(re)
'''
result = list()
        if not buildings:
            return result
        index, nows, index_buildingd = buildings[0][0], list([buildings[0]]), 1
        while nows or index_buildingd < len(buildings):
            while index_buildingd < len(buildings) and buildings[index_buildingd][
                0] == index:
                nows.append(buildings[index_buildingd])
                index_buildingd += 1
            nows = list(filter(lambda x: x[1] != index, nows))
            height = 0
            for i, now in enumerate(nows):
                if now[2] > height:
                    height = now[2]
            if not result or result[-1][1] != height:
                result.append([index, height])
            index += 1
        return result
        超时
'''
