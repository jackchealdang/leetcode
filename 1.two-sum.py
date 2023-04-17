#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for x in range(len(nums)):
            complement = target-nums[x]
            if complement in nums and nums.index(complement) != x:
                return (x, nums.index(complement))


# @lc code=end
