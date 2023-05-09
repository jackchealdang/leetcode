#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            nonlocal maxDiameter
            if not root:
                return 0

            # DFS through the left and right nodes
            left = dfs(root.left)
            right = dfs(root.right)

            # If at any point max diameter is greater, update it
            maxDiameter = max(maxDiameter, left + right)

            # Return the height to previous recursion or root
            return 1 + max(left, right)

        maxDiameter = 0
        dfs(root)
        return maxDiameter

# @lc code=end
