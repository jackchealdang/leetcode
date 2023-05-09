#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for n in nums:
            if n not in seen:
                seen.add(n)
            else:
                return True

        return False

# @lc code=end
