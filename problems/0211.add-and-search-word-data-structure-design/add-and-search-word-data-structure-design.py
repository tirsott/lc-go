class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word_list = {}


    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        if not self.word_list.get(len(word)):
            self.word_list[len(word)] = []
        self.word_list[len(word)].append(word)


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        for w in self.word_list.get(len(word), []):
            if self.compare(w, word):
                return True
        return False

    def compare(self, word1, word2):
        if len(word1) != len(word2):
            return False
        for i in range(len(word1)):
            if word1[i] == '.' or word2[i] == '.' or word1[i] == word2[i]:
                continue
            else:
                return False
        return True



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)