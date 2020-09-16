from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def dfs(exist_nums, left_s, res):
            if len(exist_nums) == 4 and left_s == '' and '.'.join(exist_nums)\
                    not in res:
                res.append('.'.join(exist_nums))
                return
            elif len(exist_nums) == 4 or not left_s:
                return
            if left_s[0] == '0':
                return dfs(exist_nums + ['0'], left_s[1:], res)
            else:
                for i in range(3):
                    if 0 < int(left_s[:i+1]) <= 255:
                        dfs(exist_nums+[left_s[:i+1]], left_s[i+1:], res)
        res = []
        dfs([], s, res)
        return res



# "25525511135"
print(Solution().restoreIpAddresses("1111"))