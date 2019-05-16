class Node():
    def __init__(self):
        self.next = dict()
        self.is_word = False


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        now = self.root
        for char_word in word:
            if char_word in now.next.keys():
                now = now.next[char_word]
            else:
                node = Node()
                now.next[char_word] = node
                now = node
        now.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        now = self.root
        for char_word in word:
            if char_word in now.next.keys():
                now = now.next[char_word]
            else:
                return False
        return now.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        now = self.root
        for char_word in prefix:
            if char_word in now.next.keys():
                now = now.next[char_word]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# class Trie(object):
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.result = list()
#
#     def insert(self, word):
#         """
#         Inserts a word into the trie.
#         :type word: str
#         :rtype: None
#         """
#         self.result.append(word)
#
#     def search(self, word):
#         """
#         Returns if the word is in the trie.
#         :type word: str
#         :rtype: bool
#         """
#         return word in self.result
#
#     def startsWith(self, prefix):
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         :type prefix: str
#         :rtype: bool
#         """
#         for word in self.result:
#             if prefix in word and word.index(prefix) == 0:
#                 return True
#         return False
