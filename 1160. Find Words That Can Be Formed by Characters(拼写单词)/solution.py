import collections
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_dict = collections.Counter(chars)
        result = 0
        for word in words:
            is_study = True
            chars_dict_now = chars_dict.copy()
            for wor in word:
                if wor in chars_dict_now:
                    chars_dict_now[wor] -= 1
                    if chars_dict_now[wor] < 1:
                        chars_dict_now.pop(wor)
                else:
                    is_study = False
                    break
            result += len(word) if is_study else 0
        return result


if __name__ == '__main__':
    so = Solution()
    words = ["cat", "bt", "hat", "tree"]
    chars = "atach"
    print(so.countCharacters(words, chars))
