# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ret = True
        def dfs(root) -> int:
            if not root:
                return 0
            right = dfs(root.right)
            left = dfs(root.left)
            if abs(right - left) < 2:
                return 1 + max(right, left)
            else:
                self.ret = False
                return 1
        dfs(root)
        return self.ret
        
        
        