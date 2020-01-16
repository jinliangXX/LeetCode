from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result, left, right = list(), 0, 0
        if not s or not p:
            return result
        map_p = Counter(p)
        map_s = dict()
        nddes, lenght = len(map_p), 0
        while right < len(s):
            if s[right] in map_p:
                map_s[s[right]] = map_s.get(s[right], 0) + 1
                if map_s[s[right]] == map_p[s[right]]:
                    lenght += 1
            if lenght == nddes:
                while left <= right:
                    if right - left + 1 == len(p):
                        result.append(left)
                    if s[left] in map_s:
                        map_s[s[left]] -= 1
                        if map_s[s[left]] < map_p[s[left]]:
                            lenght -= 1
                            if lenght < nddes:
                                break
                    left += 1
                left += 1
            right += 1
        return result


'''
    def get_num(self, n, nums):
        num_map = Counter(nums)
        result = 0
        for i in range(10 ** 6):
            if i not in num_map:
                continue
            while num_map[i] >= 2:
                num_map[i] -= 2
                num_map[i + 1] = num_map.get(i + 1, 0) + 1
            if num_map[i] == 1:
                result += 1
        return result
        '''

if __name__ == '__main__':
    so = Solution()
    so.findAnagrams('cbaebabacd', 'abc')
