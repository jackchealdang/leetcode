#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s1 = ''.join(filter(str.isalnum, s)).upper()
        # if s1 == s1[::-1]:
        #     return True
        # return False

        # Two Pointer solution

        l, r = 0, len(s) - 1

        while l < r:
            # Inner while loops skip over non-alphanumeric characters
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1

        return True
# @lc code=end
