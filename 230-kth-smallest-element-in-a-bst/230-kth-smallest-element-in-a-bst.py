# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def dfs(root):
            if not root:
                return []
            
            return [*dfs(root.left),root.val,*dfs(root.right)]
        
 
        lst=dfs(root)
        
        return lst[k-1]