from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        if not strs:
            return res
        shortest_length = min([len(str) for str in strs])
        for i in range(shortest_length):
            for str in strs:
                if str[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["dog","racecar","car"]))