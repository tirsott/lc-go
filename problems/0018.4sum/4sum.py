from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        res = []
        if n > 3:
            last_two = nums[-1] + nums[-2]
            last_three = last_two + nums[-3]
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            num1 = nums[i]
            if num1 + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if num1 + last_three < target:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                num2 = nums[j]
                if num1 + num2 + nums[j + 1] + nums[j + 2] > target:
                    break
                if num1 + num2 + last_two < target:
                    continue

                k = j + 1
                l = n - 1
                while k < l:
                    total_num = num1 + num2 + nums[k] + nums[l]
                    if total_num == target:
                        res.append([num1, num2, nums[k], nums[l]])
                        k += 1
                        while nums[k] == nums[k - 1] and k < l:
                            k += 1
                        l -= 1
                        while nums[l] == nums[l + 1] and k < l:
                            l -= 1
                    elif total_num > target:
                        l -= 1
                        while nums[l] == nums[l + 1] and k < l:
                            l -= 1
                    else:
                        k += 1
                        while nums[k] == nums[k - 1] and k < l:
                            k += 1

        return res

if __name__ == '__main__':
    a = [-498,-492,-473,-455,-441,-412,-390,-378,-365,-359,-358,-326,-311,-305,-277,-265,-264,-256,-254,-240,-237,-234,-222,-211,-203,-201,-187,-172,-164,-134,-131,-91,-84,-55,-54,-52,-50,-27,-23,-4,0,4,20,39,45,53,53,55,60,82,88,89,89,98,101,111,134,136,209,214,220,221,224,254,281,288,289,301,304,308,318,321,342,348,354,360,383,388,410,423,442,455,457,471,488,488]

    print(Solution().fourSum(a, -2808))