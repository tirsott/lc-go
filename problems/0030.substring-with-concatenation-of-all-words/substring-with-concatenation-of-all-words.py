from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        total_length = sum([len(word) for word in words])
        res = []
        if not s or not total_length or len(s) < total_length:
            return []
        words_dict = {}
        for word in words:
            if word not in words_dict:
                words_dict[word] = 1
            else:
                words_dict[word] += 1
        for i in range(len(s) - total_length + 1):
            word_list = [s[i:i+total_length][x:x+len(words[0])] for x in range(0, total_length,
                                                      len(words[0]))]
            words_dict_new = words_dict.copy()
            for word in word_list:
                if word in words_dict_new:
                    words_dict_new[word] -= 1
                else:
                    break
            if not any(words_dict_new.values()):
                res.append(i)
        return res

if __name__ == '__main__':
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","word"]
    print(Solution().findSubstring(s, words))
    # print(Solution().check_string_words(s, words))