class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.big = [0]
        self.small = [0]

    def addNum(self, num: int) -> None:
        self.big.append(num)
        # 调整大顶堆
        # 1
        self.adjust_down(self.big, 'big')
        # 取出最大值
        num = self.big[1]
        self.big[1] = self.big[len(self.big) - 1]
        self.big = self.big[:-1]
        # 2
        self.adjust_up(self.big, 'big')
        self.small.append(num)
        # 3
        self.adjust_down(self.small, 'small')
        if len(self.big) < len(self.small):
            num = self.small[1]
            self.small[1] = self.small[len(self.small) - 1]
            self.small = self.small[:-1]
            # 4
            self.adjust_up(self.small, 'small')
            self.big.append(num)
            # 5
            self.adjust_down(self.big, 'big')

    def findMedian(self) -> float:
        if len(self.big) > len(self.small):
            return float(self.big[1])
        else:
            return float((self.big[1] + self.small[1]) / 2)

    def adjust_down(self, list_all, str):
        leng = len(list_all) - 1
        while leng > 1:
            if leng % 2 == 0:
                root = int(leng / 2)
            else:
                root = int((leng - 1) / 2)
            if str == 'big':
                if list_all[root] < list_all[leng]:
                    now = list_all[root]
                    list_all[root] = list_all[leng]
                    list_all[leng] = now
            else:
                if list_all[root] > list_all[leng]:
                    now = list_all[root]
                    list_all[root] = list_all[leng]
                    list_all[leng] = now
            leng = root

    def adjust_up(self, list_all, str):
        root = 1
        next = 2 * root
        while next < len(list_all):
            if str == 'big':
                if next + 1 < len(list_all) and list_all[
                    next] < \
                        list_all[next + 1]:
                    next = next + 1
                if list_all[next] > list_all[root]:
                    now = list_all[root]
                    list_all[root] = list_all[next]
                    list_all[next] = now
                else:
                    break
            else:
                if next + 1 < len(list_all) and list_all[
                    next] > \
                        list_all[next + 1]:
                    next = next + 1
                if list_all[next] < list_all[root]:
                    now = list_all[root]
                    list_all[root] = list_all[next]
                    list_all[next] = now
                else:
                    break
            root = next
            next = next * 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
if __name__ == '__main__':
    so = MedianFinder()
    so.addNum(1)
    so.addNum(2)
    so.addNum(3)
    so.addNum(4)
    so.addNum(5)
    so.addNum(6)
    re = so.findMedian()
    print(re)
