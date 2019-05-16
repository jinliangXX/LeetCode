class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        result = 0
        i, j = 0, 0
        map_list = dict()
        while j < len(s):
            if s[j] not in map_list:
                map_list[s[j]] = j
                j += 1
            else:
                if j - i > result:
                    result = j - i
                i = max(map_list[s[j]] + 1, i + 1)
                map_list.pop(s[j])
        if j - i > result:
            result = j - i
        return result


'''
        if len(s) < 2:
            return len(s)
        result = 0
        i, j = 0, 0
        while j < len(s):
            if s[j] not in s[i:j]:
                j += 1
            else:
                if j - i > result:
                    result = j - i
                i += 1
        if j - i > result:
            result = j - i
        return result
'''

'''
result = 0
        str_last = '0'
        for i, char in enumerate(s):
            if len(str_last) > 1:
                now = str_last[1:]
            else:
                now = char
            for j, char_next in enumerate(
                    s[i + len(now):]):
                if char_next in now:
                    break
                else:
                    now += char_next
            str_last = now
            if len(now) > result:
                result = len(now)
        return result
'''

if __name__ == '__main__':
    so = Solution()
    so.lengthOfLongestSubstring("abcabcbb")
