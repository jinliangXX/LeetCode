from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        t_counter = Counter(t)
        return True if s_counter == t_counter else False


if __name__ == '__main__':
    so = Solution()
    re = so.isAnagram("anagram", "nagaram")
    print(re)
