class Solution:
    def threeSum_one(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = list()
        zheng = dict()
        fu = dict()
        zero = list()
        for num in nums:
            if num < 0:
                if num in fu.keys():
                    fu[num] += 1
                else:
                    fu[num] = 1
            elif num > 0:
                if num in zheng.keys():
                    zheng[num] += 1
                else:
                    zheng[num] = 1
            else:
                zero.append(num)
        # 全为0的情况
        if len(zero) >= 3:
            result.append([0, 0, 0])
        # 有一个零的情况 & 没有零的情况
        for key in fu.keys():
            if len(zero) >= 1:
                if -key in zheng.keys():
                    result.append([0, key, -key])
            for zheng_key in zheng.keys():
                if zheng_key >= -key:
                    continue
                if zheng.get(
                        zheng_key) > 1 and zheng_key * 2 == -key:
                    result.append(
                        [key, zheng_key, zheng_key])
                if (-key - zheng_key) != zheng_key and (
                        -key - zheng_key) in zheng.keys():
                    if [key, zheng_key,
                        -key - zheng_key] not in result and [
                        key, -key - zheng_key,
                        zheng_key] not in result:
                        result.append(
                            [key, zheng_key,
                             -key - zheng_key])
        for key in zheng.keys():
            for fu_key in fu.keys():
                if -fu_key >= key:
                    continue
                if fu.get(
                        fu_key) > 1 and fu_key * 2 == -key:
                    result.append(
                        [key, fu_key, fu_key])
                if (-key - fu_key) != fu_key and (
                        -key - fu_key) in fu.keys():
                    if [key, fu_key,
                        -key - fu_key] not in result and [
                        key, -key - fu_key,
                        fu_key] not in result:
                        result.append(
                            [key, fu_key, -key - fu_key])
        return result

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 升序排序
        num_list = sorted(nums)
        result = list()
        max_index = len(num_list) - 1
        for i, num in enumerate(num_list):
            if num > 0:
                break
            if i > 0 and num_list[i - 1] == num:
                continue
            left = i + 1
            right = max_index
            while left < right and num_list[right] >= 0:
                num_right = num_list[right]
                if right < max_index and num_right == \
                        num_list[right + 1]:
                    right -= 1
                    continue
                num_left = num_list[left]
                if -(num_left + num) > num_right:
                    left = left + 1
                elif -(num_left + num) < num_right:
                    right -= 1
                else:
                    result.append([num, num_left,
                                   num_right])
                    right -= 1
        return result


if __name__ == '__main__':
    test = [0, 0, 0]
    solution = Solution()
    result = solution.threeSum(test)
    print("result:{}".format(result))
