#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''.join(filter(str.isalnum, s)).upper()
        if s1 == s1[::-1]:
            return True
        return False
# @lc code=end
