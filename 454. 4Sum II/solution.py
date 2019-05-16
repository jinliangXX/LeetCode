class Solution:
    def fourSumCount_one(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        N = len(A)
        if N == 0:
            return 0
        nums = list()
        nums.extend(A + B + C + D)
        names = ['A', 'B', 'C', 'D']
        num_list = list()
        for i, num in enumerate(nums):
            num_list.append([num, names[int(i / N)]])
        num_sort = sorted(num_list, key=lambda x: x[0])
        result = self.Nsum(4, num_sort, 0,
                           len(num_sort) - 1, 0, [])
        return result

    def Nsum(self, N, num_sort, left, right, target,
             num_not):
        result = 0
        if N == 2:
            while left < right:
                # if num_sort[left][1] in num_not:
                #     left += 1
                #     continue
                # if num_sort[right][1] in num_not:
                #     right -= 1
                #     continue
                if num_sort[left][0] + num_sort[
                    right][0] < target:
                    left += 1
                elif num_sort[left][0] + num_sort[
                    right][0] > target:
                    right -= 1
                else:
                    result += 1
                    if num_sort[left][1] in num_not + [
                        num_sort[right][1]]:
                        result -= 1
                    right -= 1
            return result
        else:
            if target < num_sort[left][0] * N or target > \
                    num_sort[right][
                        0] * N or right - left + 1 < N:
                return result
            for i, num in enumerate(num_sort):
                if i < left or num[1] in num_not:
                    continue
                get_resu = self.Nsum(N - 1, num_sort, i,
                                     right, target - num[0],
                                     num_not + [num[1]])
                result += get_resu
            return result

    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        result = 0
        num_dict = dict()
        for a in A:
            for b in B:
                num = a + b
                if num in num_dict.keys():
                    num_dict[num] += 1
                else:
                    num_dict[num] = 1

        for c in C:
            for d in D:
                num = c + d
                if -num in num_dict.keys():
                    result += num_dict[-num]
        return result


if __name__ == '__main__':
    A = [0, 1, -1]
    B = [-1, 1, 0]
    C = [0, 0, 1]
    D = [-1, 1, 1]
    solution = Solution()
    result = solution.fourSumCount(A, B, C, D)
    print("result:{}".format(result))
