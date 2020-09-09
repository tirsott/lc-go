class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = -1
        d = {c: t.count(c) for c in t}
        res = ""
        while r < len(s):
            print(l, r, d, res)
            if r == len(s) - 1 and self.need(d.values()):
                break
            while self.need(d.values()) and r < len(s) - 1:
                r += 1
                if s[r] in t:
                    d[s[r]] -= 1
            if not self.need(d.values()):
                if res == "" or len(s[l:r+1]) < len(res):
                    res = s[l:r+1]
            if l < len(s) - 1:
                cp
                l += 1
                while l < len(s) - 1 and s[l] not in t:
                    l += 1
            else:
                break
        return res

    def need(self, count):
        for c in count:
            if c > 0:
                return True
        return False

print(Solution().minWindow("ab", "b"))