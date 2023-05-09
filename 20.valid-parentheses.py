#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        closeToOpen = {')': '(', ']': '[', '}': '{'}

        for n in s:
            if n in closeToOpen:
                if stack and stack[-1] == closeToOpen[n]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(n)

        return True if not stack else False

# @lc code=end
