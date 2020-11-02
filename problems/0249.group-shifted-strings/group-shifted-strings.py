from typing import List

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        d = {}
        for string in strings:
            distance = tuple(self.distance(string))
            if distance in d:
                d[distance].append(string)
            else:
                d[distance] = [string]
        return list(d.values())




    def distance(self, string):
        distance = []
        for i in range(len(string)):
            if string[i] == 'z' and string[i-1] == 'a':
                distance.append(25)
            elif string[i] == 'a' and string[i-1] == 'z':
                distance.append(1)
            else:
                if ord(string[i])-ord(string[i-1]) >= 0:
                    distance.append(ord(string[i])-ord(string[i-1]))
                else:
                    distance.append(26 + (ord(string[i]) - ord(string[i - 1])))
        return distance

print(Solution().groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))

# 输入：["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
# 输出：
# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]
# 解释：可以认为字母表首尾相接，所以 'z' 的后续为 'a'，所以 ["az","ba"] 也满足 “移位” 操作规律。
