class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle is None:
            return 0
        for i in range(len(haystack) - len(needle)):
            if needle == haystack[i:i+len(needle)]:
                return i
        if needle == haystack[-len(needle):]:
            return len(haystack)-len(needle)
        return -1
