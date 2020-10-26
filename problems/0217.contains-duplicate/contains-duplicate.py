from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        char_dict = {}
        for num in nums:
            if char_dict.get(num):
                return True
            else:
                char_dict[num] = 1
        return False