from typing import List
import time as tt

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        neighbor = [[] for _ in range(len(wordList))]
        start = [i for i in range(len(wordList)) if self.word_diff(beginWord,
                                                                   wordList[i])]
        end = [i for i in range(len(wordList)) if self.word_diff(endWord,
                                                                 wordList[i])]
        d = {}
        for i in range(len(wordList)):
            for j in range(len(wordList[i])):
                if wordList[i][:j] + '*' + wordList[i][j+1:] not in d:
                    d[wordList[i][:j] + '*' + wordList[i][j+1:]] = [i]
                else:
                    d[wordList[i][:j] + '*' + wordList[i][j + 1:]].append(i)

        for k, v in d.items():
            for i in range(len(v)):
                neighbor[v[i]] = list(set(neighbor[v[i]] + v[:i] + v[i+1:]))
        time = 2
        if wordList.index(endWord) in start:
            return time
        while 1:
            if [x for x in start if x in end]:
                return time + 1
            for i in start:
                if not neighbor[i]:
                    neighbor[i] = [x for x in range(len(wordList)) if
                                   self.word_diff(
                                       wordList[i], wordList[x])]
            for i in end:
                if not neighbor[i]:
                    neighbor[i] = [x for x in range(len(wordList)) if
                                   self.word_diff(
                                       wordList[i], wordList[x])]
            temp_start = list(set([x for j in [neighbor[i] for i in start] for
                                 x in j] + start))

            temp_end = list(set([x for j in [neighbor[i] for i in end] for
                                 x in j] + end))
            if [x for x in temp_start if x in end] or [x for x in temp_end if
                                                       x in start]:
                return time + 2
            if [x for x in temp_start if x in temp_end]:
                return time + 3
            if temp_start == start and temp_end == end:
                return 0
            time += 2
            start = temp_start
            end = temp_end


    def word_diff(self, a ,b):
        count = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
                if count > 1:
                    return False
        return count == 1


#beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
t = tt.time()
print(Solution().ladderLength("hit",
"cog",
["hot","dot","dog","lot","log","cog"]))

print(tt.time()-t)