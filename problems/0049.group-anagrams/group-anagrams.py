from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}
        for s in strs:
            if ''.join(sorted(s)) not in mapping:
                mapping[''.join(sorted(s))] = [s]
            else:
                mapping[''.join(sorted(s))].append(s)
        return [v for v in mapping.values()]




print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))