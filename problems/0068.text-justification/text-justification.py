from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        temp = ''
        while words:
            if temp == '':
                temp += words.pop(0)
            elif len(temp) + 1 + len(words[0]) <= maxWidth:
                temp += ' ' + words.pop(0)
            else:
                word_list = temp.split(' ')
                word_count = len(word_list)
                word_length = sum(len(word) for word in word_list)
                blank = maxWidth - word_length
                if word_count == 1:
                    res.append(temp + ' ' * (blank))
                else:
                    blank_list = [blank // (word_count-1) for _ in range(
                        word_count-1)]
                    for i in range(blank % (word_count-1)):
                        blank_list[i] += 1
                    blank_list.append(0)
                    for i in range(word_count):
                        word_list[i] += ' ' * blank_list[i]
                    res.append(''.join(word_list))
                temp = ''
        if temp:
            res.append(temp + ' ' * (maxWidth-len(temp)))
        return res

words = ["What","must","be","acknowledgment","shall","be"]
print(Solution().fullJustify(words, 16))