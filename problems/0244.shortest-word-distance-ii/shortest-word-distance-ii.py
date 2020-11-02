from typing import List

class WordDistance:

    def __init__(self, words: List[str]):
        self.position = self._get_position(words)

    def _get_position(self, words):
        position = {}
        for i in range(len(words)):
            if words[i] in position:
                position[words[i]].append(i)
            else:
                position[words[i]] = [i]
        return position

    def shortest(self, word1: str, word2: str) -> int:
        return min([abs(x - y) for x in self.position[word1] for y in
                    self.position[word2]])


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)