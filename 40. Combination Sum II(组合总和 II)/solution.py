from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = set()
        if not candidates:
            return list(result)

        def get_result(num: int, index: int, now: List):
            if num == 0 and now:
                result.add(','.join(str(i) for i in now))
                return 0
            if index < 0:
                return 0

            if candidates[index] <= num:
                copy_now = now.copy()
                copy_now.append(candidates[index])
                get_result(num - candidates[index], index - 1, copy_now)
            # 不采用当前的值
            get_result(num, index - 1, now)

        candidates.sort()
        for i in range(len(candidates) - 1, -1, -1):
            if candidates[i] <= target:
                get_result(target - candidates[i], i - 1, [candidates[i]])
        out = list()
        for re in result:
            out.append(re.split(','))
            out[-1] = [int(i) for i in out[-1]]
        return out


if __name__ == '__main__':
    so = Solution()
    candidates = [1]
    target = 1
    result = so.combinationSum2(candidates, target)
    print(result)
