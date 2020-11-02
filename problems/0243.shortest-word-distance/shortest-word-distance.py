from typing import List

class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        last_word1 = -1
        last_word2 = -1
        res = 0
        for i in range(len(words)):
            if words[i] == word1:
                last_word1 = i
                if last_word2 >= 0:
                    if res == 0:
                        res = i - last_word2
                    else:
                        res = min(res, i-last_word2)
            if words[i] == word2:
                last_word2 = i
                if last_word1 >= 0:
                    if res == 0:
                        res = i - last_word1
                    else:
                        res = min(res, i-last_word1)
        return res

print(Solution().shortestDistance(["practice", "makes", "perfect", "coding", "makes"], 'pluma', 'holm'))


# 示例:
# 假设 words = ["practice", "makes", "perfect", "coding", "makes"]
#
# 输入: word1 = “coding”, word2 = “practice”
# 输出: 3
#
# 输入: word1 = "makes", word2 = "coding"
# 输出: 1
#
