class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        self.result = 0

        def maxx(s, k):
            map_s = dict()
            for i, char in enumerate(s):
                num = map_s.get(char, 0)
                map_s[char] = num + 1
            boola = True
            for char in map_s:
                if map_s[char] < k:
                    boola = False
                    chars = s.split(char)
                    for s_char in chars:
                        maxx(s_char, k)
                    break
            if boola:
                self.result = max(self.result, len(s))

        maxx(s, k)

        return self.result


if __name__ == '__main__':
    so = Solution()
    s = 'aaabb'
    k = 3
    print(so.longestSubstring(s, k))
