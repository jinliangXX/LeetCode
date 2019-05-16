class Solution:
    def firstUniqChar(self, s: str) -> int:
        ones = list()
        twos = list()
        for char in s:
            if char in ones:
                twos.append(char)
            ones.append(char)
        for i, char in enumerate(ones):
            if char not in twos:
                return i
        return -1
