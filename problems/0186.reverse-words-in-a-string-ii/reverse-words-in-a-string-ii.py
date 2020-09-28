from typing import List

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        left, right = 0, 0
        while right < len(s):
            while right < len(s) and s[right] != ' ':
                right += 1
            for i in range((right-left)//2):
                s[left+i], s[right-1-i] = s[right-1-i], s[left+i]
            right += 1
            left = right



# 输入: ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# 输出: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
#
s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Solution().reverseWords(s)
print(s)