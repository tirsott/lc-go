class Solution:
    def canWin(self, s: str) -> bool:
        if '++' not in s:
            return False
        for idx in range(len(s)-1):
            if s[idx:idx+2]=='++':
                if not self.canWin(s[0:idx]+'--'+s[idx+2:]):
                    return True
        return False



# 输入: s = "++++"
# 输出: true
# 解析: 起始玩家可将中间的 "++" 翻转变为 "+--+" 从而得胜。