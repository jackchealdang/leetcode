#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = len(nums)//2

        while len(nums) > 1:
            if nums[idx] > target:
                nums = nums[0:idx]
            elif nums[idx] < target:
                nums = nums[idx:len(nums)+1]
            idx = len(nums)//2
            if nums[idx] == target:
                return idx
            print(idx)

        return -1
# @lc code=end
