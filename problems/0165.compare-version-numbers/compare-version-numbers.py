class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        for i in range(min(len(v1), len(v2))):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
        end = min(len(v1), len(v2))
        if len(v1) < len(v2):
            v1.extend(['0' for _ in range(len(v2)-len(v1))])
        if len(v1) > len(v2):
            v2.extend(['0' for _ in range(len(v1)-len(v2))])
        for i in range(end, len(v1)):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
        return 0





# 输入：version1 = "1.01", version2 = "1.001"
# 输出：0
# 解释：忽略前导零，“01” 和 “001” 表示相同的数字 “1”。
#
print(Solution().compareVersion("1.0.1", "1"))