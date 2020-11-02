class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # l1 = []
        # l2 = []
        # for i in range(len(s)):
        #     if s[i] == t[i]:
        #         continue
        #     else:
        #         if s[i] in l2:
        #             l2.remove(s[i])
        #         else:
        #             l1.append(s[i])
        #         if t[i] in l1:
        #             l1.remove(t[i])
        #         else:
        #             l2.append(t[i])
        #         if len(l1) > len(s) - i or len(l2) > len(s) - i:
        #             return False
        # return l1 == []
        return sorted(s) == sorted(t)


print(Solution().isAnagram(s = "rat", t = "car"))