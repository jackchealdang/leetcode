#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # s_letters = {}
        # t_letters = {}

        # for x in range(len(s)):
        #     if s[x] not in s_letters:
        #         s_letters.update({s[x]: 1})
        #     else:
        #         s_letters.update({s[x]: s_letters[s[x]]+1})
        #     if t[x] not in t_letters:
        #         t_letters.update({t[x]: 1})
        #     else:
        #         t_letters.update({t[x]: t_letters[t[x]]+1})

        s = ''.join(sorted(s))
        t = ''.join(sorted(t))

        if s == t:
            return True

        return False


# @lc code=end
