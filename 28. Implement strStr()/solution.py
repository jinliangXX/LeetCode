class Solution(object):

    def get_nextval(self, t: str) -> list:
        nextval = list()
        i, j = 0, -1
        nextval.append(j)
        while i < len(t) - 1:
            if j == -1 or t[i] == t[j]:
                i += 1
                j += 1
                if t[i] == t[j]:
                    nextval.append(nextval[j])
                else:
                    nextval.append(j)
            else:
                j = nextval[j]
        return nextval

    def index_KMP(self, s: str, t: str, pos: int) -> int:
        '''
        返回子串t在串s中第pos个字符之后的位置，不存在返回-1
        '''
        next = self.get_nextval(t)
        i, j = pos, 0
        while i < len(s) and j < len(t):
            if j == -1 or s[i] == t[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        if j == len(t):
            return i - j
        else:
            return -1

    def get_next(self, t: str) -> list:
        next = list()
        i, j = 0, -1
        next.append(j)
        while i < len(t) - 1:
            if j == -1 or t[i] == t[j]:
                i += 1
                j += 1
                next.append(j)
            else:
                j = next[j]
        return next

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return self.index_KMP(haystack, needle, 0)
