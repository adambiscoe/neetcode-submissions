# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
      self.m = 0
      def dfs(root):
         if not root:
            return 0
         right = dfs(root.right)
         left = dfs(root.left)
         val = dfs(root.right) + dfs(root.left)
         if val > self.m:
            self.m = val
         return 1 + max(right, left)
      dfs(root)
      return self.m

        
        