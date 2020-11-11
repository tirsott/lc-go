from typing import List

class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.d = {}
        self.dictionary = dictionary
        for word in list(set(dictionary)):
            if len(word) <= 2:
                continue
            if word[0] + str(len(word)-2) + word[-1] not in self.d:
                self.d[word[0] + str(len(word)-2) + word[-1]] = 1
            else:
                self.d[word[0] + str(len(word) - 2) + word[-1]] += 1


    def isUnique(self, word: str) -> bool:
        if len(word) <= 2:
            return True
        if self.d.get(word[0] + str(len(word) - 2) + word[-1], 0) == 0:
            return True
        elif self.d.get(word[0] + str(len(word) - 2) + word[-1], 0) == 1:
            return word in self.dictionary
        else:
            return False


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)