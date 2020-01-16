from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = list()
        if not candidates:
            return result

        def get_result(num: int, index: int, now: List):
            if index < 0:
                return 0
            if num == 0 and now:
                result.append(now)
                return 0

            # # 从当前开始
            # if candidates[index] <= target:
            #     get_result(target - candidates[index], index,
            #                [candidates[index]])
            # 采用当前的值
            if candidates[index] <= num:
                copy_now = now.copy()
                copy_now.append(candidates[index])
                get_result(num - candidates[index], index, copy_now)
            # 不采用当前的值
            get_result(num, index - 1, now)

        for i in range(len(candidates) - 1, -1, -1):
            if candidates[i] <= target:
                get_result(target - candidates[i], i, [candidates[i]])
        return result


if __name__ == '__main__':
    so = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    result = so.combinationSum(candidates, target)
    print(result)
