from typing import List

class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        p1 = []
        p2 = []
        for i in range(len(words)):
            if words[i] == word1:
                p1.append(i)
            if words[i] == word2:
                p2.append(i)
        if word1 == word2:
            return min([p1[i+1]-p1[i] for i in range(len(p1)-1)])
        else:
            return min([abs(x - y) for x in p1 for y in
                        p2])




# 示例:
# 假设 words = ["practice", "makes", "perfect", "coding", "makes"].
#
# 输入: word1 = “makes”, word2 = “coding”
# 输出: 1
#
# 输入: word1 = "makes", word2 = "makes"
# 输出: 3
