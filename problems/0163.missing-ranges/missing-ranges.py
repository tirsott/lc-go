from  typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if not nums or nums[0] > lower:
            nums.insert(0, lower-1)
        if nums[-1] < upper:
            nums.append(upper+1)
        res = []
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                continue
            elif nums[i+1] - nums[i] == 2:
                res.append(str(nums[i]+1))
            else:
                res.append('{}->{}'.format(nums[i]+1, nums[i+1]-1))
        return res



# 给定一个排序的整数数组 nums ，其中元素的范围在 闭区间 [lower, upper] 当中，返回不包含在数组中的缺失区间。
#
# 示例：
#
# 输入: nums = [0, 1, 3, 50, 75], lower = 0 和 upper = 99,
# 输出: ["2", "4->49", "51->74", "76->99"]
#
print(Solution().findMissingRanges([], 1, 1))